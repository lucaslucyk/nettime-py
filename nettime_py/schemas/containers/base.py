from typing import Optional, TypeVar
from typing import Optional
from pydantic import Field

from nettime_py.schemas.base import Base as BaseSchema


class Base(BaseSchema):
    id: Optional[int] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


ListModel = TypeVar("ListModel", bound=Base)
DetailModel = TypeVar("DetailModel", bound=Base)
