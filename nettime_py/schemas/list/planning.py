from typing import Optional
from pydantic import Field
from datetime import datetime
from ..base import Base


class Planning(Base):
    state_description: Optional[str] = Field(
        default=None, alias="stateDescription"
    )
    describe: Optional[str] = Field(default=None, alias="describe")
    employeeName: Optional[str] = Field(default=None, alias="employeeName")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    confirm_by: Optional[str] = Field(default=None, alias="confirmBy")
    incidencia_futura_total_docs: Optional[int] = Field(
        default=None, alias="IncidenciaFutura.totalDocs"
    )
    confirm: Optional[datetime] = Field(default=None, alias="confirm")
    created: Optional[datetime] = Field(default=None, alias="created")
    last_day: Optional[datetime] = Field(default=None, alias="lastDay")
    first_day: Optional[datetime] = Field(default=None, alias="firstDay")
    has_comment: Optional[bool] = Field(default=None, alias="hasComment")
    describe_TT: Optional[str] = Field(default=None, alias="describeTT")
    num_days: Optional[int] = Field(default=None, alias="numDays")
