from typing import Optional

from pydantic import Field
from ..base import Base


class Reader(Base):
    get_full_path: Optional[str] = Field(default=None, alias="GetFullPath")
    profaceX_SN: Optional[str] = Field(default=None, alias="ProfaceXSN")
