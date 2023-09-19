from typing import Optional
from pydantic import BaseModel, Field


class AppIndex(BaseModel):
    version: Optional[str] = Field(default=None, alias="version")
    name: Optional[str] = Field(default=None, alias="name")
    activated: Optional[bool] = Field(default=None, alias="activated")
    show_supervisor_on_login: Optional[bool] = Field(
        default=None,
        alias="showSupervisorOnLogin"
    )
    hide_login_form: Optional[bool] = Field(default=None, alias="hideLoginForm")
    product: Optional[str] = Field(default=None, alias="product")
    portal: Optional[bool] = Field(default=None, alias="portal")
    can_change_password: Optional[bool] = Field(
        default=None,
        alias="canChangePassword"
    )
    qa_message: Optional[str] = Field(default=None, alias="qaMessage")
    saas: Optional[bool] = Field(default=None, alias="saas")
    update_ver: Optional[bool] = Field(default=None, alias="updateVer")