from datetime import date
from typing import Any, Dict
from pydantic_settings import BaseSettings


ACTION_SAVE = "Save"
ACTION_DELETE = "Delete"
ACTION_COPY = "Copy"
ACTION_EDIT_FORM = "editForm"
ACTION_VIEW = "View"


class Defaults(BaseSettings):
    TASK_LOOP_TIME: float = 0.5
    PAGE_SIZE: int = 50
    TIME_OUT: int = 60
    DATE_FROM: date = date.today()

    SESSION_HEADERS: Dict[str, Any] = {
        "DNT": "1",
        "Accept-Encoding": "gzip,deflate",
        "User-Agent": "netTime API Python"
        # "Content-Type": "application/json;charset=UTF-8"
    }
    
    class Extra:
        ...