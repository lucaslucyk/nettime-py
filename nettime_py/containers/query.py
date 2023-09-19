import datetime as dt
from pydantic import BaseModel, Field, validator
from typing import List


class QueryField(BaseModel):
    name: str
    start_date: dt.date = Field(default=dt.date.today(), alias="startDate")

    def __str__(self) -> str:
        return self.model_dump_json(
            by_alias=True
        ).replace("'", '"').replace(" ", "")


class Query(BaseModel):

    fields: List[QueryField] = Field(default=[
        QueryField(name="id"),
        QueryField(name="name")
    ])
    filter_exp: str = Field(alias="filterExp", default="")

    def __str__(self) -> str:
        return self.model_dump_json(by_alias=True).replace(" ", "")
    
    @validator("filter_exp")
    def _filter_exp_validator(cls, value: str) -> str:
        return value.replace('"', "'")