from typing import Optional, Sequence, Tuple, TypeVar, Union
from typing import Optional
from pydantic import BaseModel, Field


class Base(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")

    @property
    def _extra(self) -> set[str]:
        return set(self.__dict__) - set(self.__fields__)

    @property
    def alias_fields(self) -> Sequence[Union[str, None]]:
        # for field in self.model_fields.values():
        #     yield getattr(field, "alias", None)
        return tuple(
            getattr(field, "alias", None)
            for field in self.model_fields.values()
        )
    
    @classmethod
    def get_alias_fields(cls) -> Sequence[Union[str, None]]:
        return tuple(
            getattr(field, "alias", None)
            for field in cls.model_fields.values()
        )

    class Config:
        extra = "allow"


ListModel = TypeVar("ListModel", bound=Base)
DetailModel = TypeVar("DetailModel", bound=Base)
