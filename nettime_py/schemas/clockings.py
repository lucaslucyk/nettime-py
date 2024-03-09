import datetime as dt
from enum import Enum
from typing import List, Optional
from pydantic import Field
from nettime_py.schemas.base import Base as BaseSchema


class PetitionAction(str, Enum):
    Change = "Change"


class PetitionActions(BaseSchema):
    actions: Optional[List[PetitionAction]] = Field(
        default=None,
        alias="actions",
    )


class StatusAction(str, Enum):
    Delete = "Delete"
    Edit = "Edit"
    Comment = "Comment"


class ClockingStatus(BaseSchema):
    effective: Optional[bool] = Field(default=None, alias="effective")
    desc: Optional[str] = Field(default=None, alias="desc")
    state: Optional[str] = Field(default=None, alias="state")
    entering: Optional[bool] = Field(default=None, alias="entering")
    actions: Optional[List[StatusAction]] = Field(default=None, alias="actions")


class Clocking(BaseSchema):
    id: Optional[int] = Field(default=None, alias="id")
    date: Optional[dt.datetime] = Field(default=None, alias="date")
    id_elem: Optional[int] = Field(default=None, alias="idElem")
    type: Optional[str] = Field(default=None, alias="type")
    id_reader: Optional[int] = Field(default=None, alias="idReader")
    user: Optional[str] = Field(default=None, alias="user")
    ip: Optional[str] = Field(default=None, alias="ip")
    status: Optional[ClockingStatus] = Field(default=None, alias="status")
    app: Optional[bool]
    num_documents: Optional[int] = Field(default=None, alias="numDocuments")


class DayInfo(BaseSchema):
    change: Optional[str] = Field(default="Change", alias="Change")
    delete: Optional[str] = Field(default="Delete", alias="Delete")
    edit: Optional[str] = Field(default="Edit", alias="Edit")
    comment: Optional[str] = Field(default="Comment", alias="Comment")


class Day(BaseSchema):
    date: Optional[dt.date] = Field(default=None, alias="date")
    id_emp: Optional[int] = Field(default=None, alias="idEmp")
    shift: Optional[int] = Field(default=None, alias="shift")
    min_fin: Optional[int] = Field(default=None, alias="minFin")
    min_fin_forced: Optional[bool] = Field(default=None, alias="minFinForced")
    shift_petition: Optional[PetitionActions] = Field(
        default=None,
        alias="shiftPetition",
    )
    clockings: Optional[List[Clocking]] = Field(default=None, alias="clockings")
    info: Optional[DayInfo] = Field(default=None, alias="info")
