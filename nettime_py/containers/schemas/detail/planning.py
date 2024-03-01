from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field
from .base import Base


class DataLabel(BaseModel):
    data: Optional[str] = Field(default=None, alias="data")
    label: Optional[str] = Field(default=None, alias="label")


class IntervalTimeTypeValidity(BaseModel):
    start: Optional[int] = Field(default=None, alias="start")
    end: Optional[int] = Field(default=None, alias="end")


class IntervalTimeType(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    validity: Optional[List[IntervalTimeTypeValidity]] = Field(
        default=None, alias="validity"
    )


class TimeInterval(BaseModel):
    can_overlap: Optional[bool] = Field(default=None, alias="canOverlap")
    time_types: Optional[List[IntervalTimeType]] = Field(
        default=None, alias="timeTypes"
    )


class Planning(Base):
    first_day: Optional[datetime] = Field(default=None, alias="firstDay")
    all_day_id: Optional[int] = Field(default=None, alias="allDayId")
    all_day: Optional[bool] = Field(default=None, alias="allDay")
    self_owner: Optional[bool] = Field(default=None, alias="selfOwner")
    state: Optional[str] = Field(default=None, alias="state")
    comments: Optional[str] = Field(default=None, alias="comments")
    int_state: Optional[int] = Field(default=None, alias="intState")
    is_accepted: Optional[bool] = Field(default=None, alias="isAccepted")
    last_day: Optional[datetime] = Field(default=None, alias="lastDay")
    num_days: Optional[int] = Field(default=None, alias="numDays")
    confirm_by: Optional[str] = Field(default=None, alias="confirmBy")
    confirm: Optional[datetime] = Field(default=None, alias="confirm")
    describe: Optional[str] = Field(default=None, alias="describe")
    has_comment: Optional[bool] = Field(default=None, alias="hasComment")
    error: Optional[str] = Field(default=None, alias="error")
    state_description: Optional[str] = Field(
        default=None, alias="stateDescription"
    )
    describe_TT: Optional[str] = Field(default=None, alias="describeTT")
    is_pending: Optional[bool] = Field(default=None, alias="isPending")
    is_validation_pending: Optional[bool] = Field(
        default=None, alias="isValidationPending"
    )
    is_denied: Optional[bool] = Field(default=None, alias="isDenied")
    total_docs: Optional[int] = Field(default=None, alias="totalDocs")
    validated_days: Optional[List[int]] = Field(
        default=None, alias="validatedDays"
    )
    date_interval: Optional[List[int]] = Field(
        default=None, alias="dateInterval"
    )
    ba_valid_elems: Optional[List[int]] = Field(
        default=None, alias="baValidElems"
    )
    time_types: Optional[List[int]] = Field(default=None, alias="timeTypes")
    nodes_source: Optional[List[DataLabel]] = Field(
        default=None, alias="nodesSource"
    )
    employee: Optional[Union[int, List[int]]] = Field(
        default=None, alias="employee"
    )
    time_intervals: Optional[TimeInterval] = Field(
        default=None, alias="timeIntervals"
    )
