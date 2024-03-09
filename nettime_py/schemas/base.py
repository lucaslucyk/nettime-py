
from typing import Sequence, Union
from pydantic import BaseModel


class Base(BaseModel):

    @property
    def _extra(self) -> set[str]:
        return set(self.__dict__) - set(self.model_fields)

    @property
    def alias_fields(self) -> Sequence[Union[str, None]]:
        return tuple(
            getattr(field, "alias", None)
            for field in self.model_fields.values()
        )

    @classmethod
    def get_alias_fields(cls) -> Sequence[Union[str, None]]:
        return tuple(
            getattr(field, "alias", None) for field in cls.model_fields.values()
        )

    class Config:
        extra = "allow"