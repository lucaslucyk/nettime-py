from abc import ABC, abstractmethod
from pydantic import TypeAdapter, validate_call
from typing import TYPE_CHECKING, Any, Generator, Generic, List, Optional
from .query import Query
from ..pagination import LimitOffsetPagination as Pagination
from ..schemas.base import ListModel, DetailModel
from ..config import (
    ACTION_VIEW,
    ACTION_SAVE,
    ACTION_SAVE_OK,
    ACTION_SAVE_ERROR,
    OFFSET_PARAM_NAME,
    LIMIT_PARAM_NAME
)
from ..exceptions import NotFoundException, SaveException


if TYPE_CHECKING:
    from ..api import NetTimeAPI


class ContainerBase(Generic[ListModel, DetailModel], ABC):
    def __init__(
        self,
        client: "NetTimeAPI",
        page_size: int = 10,
        # order: str = None
    ) -> None:
        super().__init__()
        self._client = client
        self._page_size = page_size
        self._base_path = "/api/container/"
        self._list_prefix = "elements/"
        self._action_prexix = "action/exec/"

    @property
    @abstractmethod
    def list_schema(self) -> type[ListModel]:
        ...

    @property
    @abstractmethod
    def detail_schema(self) -> type[DetailModel]:
        ...

    @property
    @abstractmethod
    def path_attribute(self) -> str:
        ...

    @property
    @abstractmethod
    def container_name(self) -> str:
        ...

    @property
    @abstractmethod
    def order(self) -> str:
        ...

    @property
    def base_params(self) -> dict:
        return {"container": self.container_name}

    @property
    def list_path(self) -> str:
        return self._base_path + self._list_prefix + self.path_attribute

    @property
    def action_path(self) -> str:
        return self._base_path + self._action_prexix + self.path_attribute

    @property
    def list_url(self) -> str:
        return self._client.url + self.list_path

    @property
    def action_url(self) -> str:
        return self._client.url + self.action_path

    @property
    def page_size(self) -> int:
        return self._page_size

    @page_size.setter
    def page_size(self, value: int) -> None:
        self._page_size = value

    def _parse_object_as(self, kind: Any, data: Any) -> Any:
        """Parse python object to pydantic model type

        Args:
            kind (Any): Pydantic model type
            data (Any): Python object

        Returns:
            Any: Pydantic model type instance
        """

        return TypeAdapter(kind).validate_python(data)

    @validate_call(config={"arbitrary_types_allowed": True})
    def list(
        self,
        offset: int = 0,
        query: Query = Query(),
        search: str = "",
        desc: bool = False,
        params: dict = {},
        **kwargs
    ) -> Pagination[ListModel]:
        """List elements of a container

        Args:
            offset (int, optional): Start offset. Defaults to 0.
            query (Query, optional):
                Fields and filter expression. Defaults to Query().
            search (str, optional):
                Arbitrary text to search in all fields. Defaults to "".
            desc (bool, optional): Desc param. Defaults to False.
            params (dict, optional):
                Custom params to send to `client.get` method. Defaults to {}.

        Returns:
            Pagination[ListModel]: Pagination of instanced ListModel.
        """

        # update custom inner params with params and page keys
        params.update(
            {
                # pagination
                OFFSET_PARAM_NAME: offset,
                LIMIT_PARAM_NAME: self.page_size,
                # args
                "query": str(query),
                "search": search,
                "desc": str(desc),
                "order": self.order,
            }
        )

        # create params from container base_params and update with inner
        _params = self.base_params
        _params.update(params)

        # get response from api client
        response = self._client.get(url=self.list_url, params=_params, **kwargs)

        # return paginator
        return Pagination(
            items=self._parse_object_as(
                kind=List[self.list_schema], data=response.get("items", [])
            ),
            container=self,
            method_name="list",
            params={"params": _params},
            offset=offset,
        )

    @validate_call(config={"arbitrary_types_allowed": True})
    def all(
        self,
        query: Query = Query(),
        search: str = "",
        desc: bool = False,
        params: dict = {},
        page: Optional[Pagination] = None,
    ) -> Generator[ListModel, Any, None]:
        """Get all elements of a container using `list` method.

        Args:
            query (Query, optional):
                Fields and filter expression. Defaults to Query().
            search (str, optional):
                Arbitrary text to search in all fields. Defaults to "".
            desc (bool, optional): Desc param. Defaults to False.
            params (dict, optional):
                Custom params to send to `client.get` method. Defaults to {}.
            page (Optional[Pagination], optional):
                Optional Pagination object to start. Defaults to None.

        Yields:
            Generator[ListModel, Any, None]: Iterator of ListModel instances.
        """

        if not page:
            # create paginator
            page = self.list(
                query=query, search=search, desc=desc, params=params
            )
            # yield elements
            for item in page:
                yield item

        # get next page
        page = page.next_page()

        # return -exit- if page is empty
        if not page:
            return
        # yield elements if not
        for item in page:
            yield item

        # try to yield next page
        yield from self.all(
            query=query, search=search, desc=desc, params=params, page=page
        )

    @validate_call(config={"arbitrary_types_allowed": True})
    def get(self, id: int, **kwargs) -> DetailModel:
        """Gets an element from the given id

        Args:
            id (int): Element id

        Raises:
            NotFoundException: If an element with the given id does not exist

        Returns:
            DetailModel: Found item
        """

        _json = self.base_params
        _json.update({"action": ACTION_VIEW, "all": False, "elements": [id]})

        res = self._client.post(url=self.action_url, json=_json, **kwargs)
        if not len(res):
            raise NotFoundException("Element not found")
        return self._parse_object_as(
            kind=self.detail_schema, data=res[0].get("dataObj")
        )

    @validate_call
    def save(self, data: DetailModel, **kwargs) -> DetailModel:
        """Save an element to netTime

        Args:
            data (DetailModel): Element to save

        Raises:
            SaveException: If something was wrong

        Returns:
            DetailModel: Updated object
        """
        
        _json = self.base_params
        _json.update(
            {
                "action": ACTION_SAVE,
                "all": False,
                "elements": [data.id],
                "dataObj": data.model_dump(
                    exclude_unset=True, by_alias=True, mode="json"
                ),
            }
        )
        res = self._client.post(url=self.action_url, json=_json, **kwargs)
        if not len(res):
            raise SaveException("Something was wrong")

        # get first and return
        res = res[0]
        # if res.get("type") == ACTION_SAVE_ERROR:
        if res.get("type") != ACTION_SAVE_OK:
            raise SaveException(res.get("message"))

        return self._parse_object_as(
            kind=self.detail_schema, data=res.get("dataObject")
        )
