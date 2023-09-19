from typing import Optional
from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    first_date: Optional[int] = Field(default=None, alias="firstDate")
    last_date: Optional[int] = Field(default=None, alias="lastDate")
    username: Optional[str] = Field(default=None, alias="username")
    default_language: Optional[str] = Field(
        default=None,
        alias="defaultLanguage"
    )
    rol: Optional[str] = Field(default=None, alias="rol")
    reader_in_clock: Optional[str] = Field(default=None, alias="readerInClock")
    logout_page: Optional[str] = Field(default=None, alias="logoutPage")
    help_page: Optional[str] = Field(default=None, alias="helpPage")
    sync_delay: Optional[int] = Field(default=None, alias="syncDelay")
    timeout_session_retry: Optional[int] = Field(
        default=None,
        alias="timeoutSessionRetry"
    )
    disable_browser_check: Optional[bool] = Field(
        default=None,
        alias="disableBrowserCheck"
    )
    keep_alive: Optional[bool] = Field(default=None, alias="keepAlive")
    session_id: Optional[str] = Field(default=None, alias="sessionId")
    product: Optional[str] = Field(default=None, alias="product")
    task_config: Optional[int] = Field(default=None, alias="taskConfig")