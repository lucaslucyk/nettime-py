from typing import Optional
from datetime import datetime
from pydantic import Field
from ..base import Base as BaseSchema


class Base(BaseSchema):
    # id: Optional[int] = Field(default=-1, alias="id")
    c_: Optional[str] = Field(default="", alias="_c_")
    created: Optional[datetime] = Field(default=None, alias="created")
    modified: Optional[datetime] = Field(default=None, alias="modified")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    modified_by: Optional[str] = Field(default=None, alias="modifiedBy")
    rev: Optional[int] = Field(default=None, alias="rev")
