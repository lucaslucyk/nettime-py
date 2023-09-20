from __future__ import annotations
import atexit
from time import sleep
from typing import Any, Optional, Union, Dict
from requests import Session, Response
from requests.exceptions import HTTPError
from pydantic import validate_call


from .exceptions import AuthException, ConfigException, UrlException
from .containers.employee import Employee
from .containers.reader import Reader
from .config import Defaults
from .schemas.app_settings import AppSettings
from .schemas.app_index import AppIndex


TASK_COMPLETED_KEY = "completed"


__all__ = ["NetTimeAPI"]


class NetTimeAPI:

    def __init__(
        self,
        url: Union[str, bytes],
        username: str,
        password: str,
        # session: Session = Session(),
        session_config: Optional[Dict[str, Any]] = None,
        aditional_headers: Optional[Dict[str, Any]] = None
    ) -> None:
        """ Create a connector with nettime app using recived parameters

        Args:
            url Union[str, bytes]: Nettime url. Eg `https://server-name:8091/`
            username (str): Nettime username
            pwd (str): Nettime password
            session (Optional[Session], optional):
                Optional session handler. Defaults to None.
        """
        self.url = url
        self._username = username
        self._password = password
        self._defaults = Defaults()
        self._session_config = session_config
        self._aditional_headers = aditional_headers

        self._check_config()

        # create and config session
        self.session = Session()
        atexit.register(self.session.close)
        self._config_session()

        self._access_token: Optional[str] = None
        self._settings: Optional[AppSettings] = None
        self._index: Optional[AppIndex] = None

    def __str__(self) -> str:
        return f'NetTime client for {self.url}'
    

    def __repr__(self) -> str:
        return "{class_}({params})".format(
            class_=type(self).__name__,
            params=', '.join([
                f'url="{self.url}"',
                f'username="{self._username}"',
                f'password="{self._password}"',
                f'session_config="{self.session_config}"',
                f'aditional_headers="{self._aditional_headers}"',
            ])
        )
    

    def __eq__(self, o: NetTimeAPI) -> bool:
        return self.url == o.url and self._username == o._username
    

    def __ne__(self, o: NetTimeAPI) -> bool:
        return self.url != o.url or self._username != o._username


    def _config_session(self) -> None:
        """Apply default headers, aditional inner headers and session config
        """

        # apply default headers
        self.session.headers.update(self._defaults.SESSION_HEADERS)
        
        # apply aditional headers
        if self._aditional_headers:
            self.session.headers.update(self._aditional_headers)
        
        # apply custom configs
        if self._session_config:
            for k,v in self._session_config.items():
                setattr(self.session, k, v)


    def _check_config(self) -> None:
        """Check inner params at instance creation.

        Raises:
            ConfigException: If params missing
        """
        if not self.url:
            raise ConfigException("Missing url in API creation")
        
        if not self._username or not self._password:
            raise ConfigException("Missing username or password")
        

    def __enter__(self, *args, **kwargs) -> NetTimeAPI:
        self.login()
        self._settings = self.settings
        self._index = self.index
        return self


    @property
    def settings(self) -> AppSettings:
        return self.get_settings()


    @property
    def index(self) -> AppIndex:
        return self.get_index()
    

    def __exit__(self, *args, **kwargs) -> None:
        if self.is_authenticated:
            self.logout()

        self.session.__exit__(*args)


    def _clear_user_session(self) -> None:
        """Deletes data associated with the user session
        """
        self._access_token = None
        self.session.headers.pop("Cookie", None)

    
    def _set_user_session(self, access_token: str) -> None:
        """Set data associated with the user session

        Args:
            access_token (str): Token received by login strategy.
        """

        self._access_token = access_token
        self.session.headers.update({
            "Cookie": f"sessionID={access_token}; i18next=es"
        })


    @property
    def is_authenticated(self) -> bool:
        """ Informs if client has headers and access_token. """
        return all((
            "Cookie" in self.session.headers.keys(),
            self._access_token != None
        ))


    def _raise_or_return_json(self, response: Response) -> Any:
        """Raise HTTPError before converting response to json

        Args:
            response (Response): Request response object

        Returns:
            Any: JSON Response
        """

        try:
            response.raise_for_status()
        except HTTPError:
            raise

        try:
            json_value = response.json()
        except ValueError:
            return response.content
        else:
            return json_value


    def get(
        self,
        url: Optional[Union[str, bytes]] = None,
        path: Optional[Union[str, bytes]] = None,
        params: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Any:
        """Sends a POST request to url or self.url + path.

        Args:
            url (Optional[Union[str, bytes]], optional):
                Full url to make request. Defaults to None.
            path (Optional[Union[str, bytes]], optional):
                Partial url to join to self.url. Defaults to None.
            data (Any, optional):
                Data to post. Defaults to None.

        Raises:
            UrlException: When a url or path is not specified

        Returns:
            Response: netTime API Response
        """

        if not url and not path:
            raise UrlException("Must specify a complete url or path")
        
        # build url
        _url = url or self.url + path
        response = self.session.get(url=_url, params=params, **kwargs)
        result = self._raise_or_return_json(response=response)
        return self._discover_task(result=result)


    def post(
        self,
        url: Optional[Union[str, bytes]] = None,
        path: Optional[Union[str, bytes]] = None,
        data: Any = None,
        json: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Any:
        """Sends a POST request to url or self.url + path.

        Args:
            url (Optional[Union[str, bytes]], optional):
                Full url to make request. Defaults to None.
            path (Optional[Union[str, bytes]], optional):
                Partial url to join to self.url. Defaults to None.
            data (Any, optional):
                Data to post. Defaults to None.
            json (Optional[Dict[str, Any]], optional):
                JSON to post. Defaults to None.

        Raises:
            UrlException: When a url or path is not specified

        Returns:
            Response: netTime API Response
        """

        if not url and not path:
            raise UrlException("Must specify a complete url or path")
        
        # build url
        _url = url or self.url + path
        response = self.session.post(url=_url, data=data, json=json, **kwargs)
        result = self._raise_or_return_json(response=response)
        return self._discover_task(result=result)
    

    def _discover_task(self, result: Any) -> Any:
        """Checks if the result is of type task and waits for it to finish 
        before returning its result.

        Args:
            result (Any): JSON response.

        Returns:
            Any: JSON response or JSON Task result.
        """
        if isinstance(result, dict) and result.get('taskId', None):
            result = self.get_task_response(task_id=result.get('taskId'))

        # return json response
        return result


    def login(self) -> None:
        """ Connect the client to set access_token and headers values. """

        if self.is_authenticated:
            return

        # remove content type from headers. Must be not json
        self._clear_user_session()
        
        # data prepare
        data = {"username": self._username, "pwd": self._password}
        # consulting nettime
        response = self.post(path='/api/login', json=data)

        if not response.get("ok", None):
            raise AuthException({
                "status": 401,
                "detail": response.get("message")
            })
        
        self._set_user_session(access_token=response.get("access_token"))


    def logout(self) -> None:
        """ Disconnect a client to clean the access_token. """

        if not self.is_authenticated:
            return

        # do logout
        self.post(path='/api/logout')

        # clean token and headers for safety
        self._clear_user_session()


    def relogin(self) -> None:
        """ Reconnect client cleaning headers and access_token. """

        self.logout()
        self.login()


    def get_task_status(self, task_id: int, **kwargs):
        """ Get status of an async task. """

        # prepare task parameters
        params = {"taskid": task_id}

        # request.get -> json
        return self.get(path='/api/async/status', params=params, **kwargs)


    def get_task_response(self, task_id: int):
        """ Return the result of a async task. """

        # ensure the task is complete
        task_status = self.get_task_status(task_id=task_id)
        while not task_status.get(TASK_COMPLETED_KEY, False):
            sleep(self._defaults.TASK_LOOP_TIME)
            task_status = self.get_task_status(task_id=task_id)

        # prepare task parameters
        params = {"taskid": task_id}

        # request.get -> json
        return self.get(path='/api/async/response', params=params)
    
    
    @validate_call(validate_return=True)
    def get_settings(self) -> AppSettings:
        """Get settings of netTime"""

        return self.get(path='/api/settings')
    
    
    @validate_call(validate_return=True)
    def get_index(self) -> AppIndex:
        """Get settings of netTime"""

        return self.get(path='/api/index')


    @property
    def employees(self) -> Employee:
        return Employee(client=self)


    @property
    def readers(self) -> Reader:
        return Reader(client=self)