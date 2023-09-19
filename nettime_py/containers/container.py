from abc import ABC, abstractmethod
from pydantic import TypeAdapter, validate_call
from typing import TYPE_CHECKING, Any, Generator, Generic, List, Optional
from .query import Query
from ..pagination import LimitOffsetPagination as Pagination
from ..schemas.base import ModelType

if TYPE_CHECKING:
    from ..api import NetTimeAPI


OFFSET_PARAM_NAME = "pageStartIndex"
LIMIT_PARAM_NAME = "pageSize"


class Container(Generic[ModelType], ABC):
    def __init__(
            self,
            client: "NetTimeAPI",
            page_size: int = 10,
            # order: str = None
        ) -> None:
        super().__init__()
        self._client = client
        self._page_size = page_size
        self._base_path = '/api/container/elements/'

    
    @property
    @abstractmethod
    def schema_class(self) -> ModelType:
        ...


    @property
    @abstractmethod
    def path_attribute(self) -> str:
        ...

    @property
    @abstractmethod
    def base_params(self) -> dict:
        ...


    @property
    def path_url(self) -> str:
        return self._base_path + self.path_attribute


    @property
    def url(self) -> str:
        return self._client.url + self.path_url
    

    @property
    def page_size(self) -> int:
        return self._page_size


    @page_size.setter
    def page_size(self, value: int) -> None:
        self._page_size = value
    

    def parse_object_as(self, kind: Any, data: Any) -> Any:
        # adapter = TypeAdapter(kind)
        return TypeAdapter(kind).validate_python(data)
        
    
    @validate_call(config={"arbitrary_types_allowed": True})
    def list(
        self,
        offset: int = 0,
        query: Query = Query(),
        search: str = "",
        desc: bool = False,
        params: dict = {}
    ) -> Pagination[ModelType]:
        params.update({
            # pagination
            OFFSET_PARAM_NAME: offset,
            LIMIT_PARAM_NAME: self.page_size,
            # args
            "query": str(query),
            "search": search,
            "desc": str(desc)
        })
        _params = self.base_params
        _params.update(params)
        response = self._client.get(url=self.url, params=_params)
        return Pagination(
            items=self.parse_object_as(
                kind=List[self.schema_class],
                data=response.get('items', [])
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
        page: Optional[Pagination] = None
    ) -> Generator[ModelType, Any, None]:        
        if not page:
            page = self.list(
                query=query,
                search=search,
                desc=desc,
                params=params
            )
            for item in page: yield item

        page = page.next_page()
        if not page: return
        for item in page: yield item
        
        yield from self.all(
            query=query,
            search=search,
            desc=desc,
            params=params,
            page=page
        )