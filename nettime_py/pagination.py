from __future__ import annotations
from typing import TYPE_CHECKING, Any, Generator, Generic, Iterable, List
from .schemas.base import ModelType

if TYPE_CHECKING:
    from .containers.base import ContainerBase


class LimitOffsetPagination(Generic[ModelType]):
    
    def __init__(
        self,
        items: Iterable,
        container: "ContainerBase",
        method_name: str,
        params: dict = {},
        offset: int = 0,
    ) -> None:
        self._items = items
        self._offset = offset
        self._container = container
        self._params = params
        self._method_name = method_name


    def __iter__(self) -> Generator[ModelType, Any, None]:
        yield from self._items


    def __len__(self) -> int:
        return len(self._items)


    def __getitem__(self, index: int) -> ModelType:
        return self._items[index]


    def __setitem__(self, index: int, value) -> None:
        self._items[index] = value


    @property
    def all(self) -> List[ModelType]:
        return self._items
    

    @property
    def page_size(self) -> int:
        return self._container.page_size


    def next_page(self) -> LimitOffsetPagination:
        self._offset += self.page_size
        return getattr(self._container, self._method_name)(
            offset=self._offset, **self._params
        )


    def prev_page(self) -> LimitOffsetPagination:
        self._offset += self.page_size
        return getattr(self._container, self._method_name)(
            offset=self._offset, **self._params
        )