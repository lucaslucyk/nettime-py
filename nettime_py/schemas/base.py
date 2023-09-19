from typing import Optional, TypeVar
from typing import Optional
from pydantic import BaseModel, Field


class Base(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)

    @property
    def _extra(self) -> set[str]:
        return set(self.__dict__) - set(self.__fields__)

    class Config:
        extra = "allow"

ModelType = TypeVar("ModelType", bound=Base)