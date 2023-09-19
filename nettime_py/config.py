from datetime import date
from typing import Any, Dict
from pydantic_settings import BaseSettings


class Defaults(BaseSettings):
    TASK_LOOP_TIME: float = 0.5
    PAGE_SIZE: int = 50
    TIME_OUT: int = 60
    DATE_FROM: date = date.today()

    SESSION_HEADERS: Dict[str, Any] = {
        "DNT": "1",
        "Accept-Encoding": "gzip,deflate",
        # "Content-Type": "application/json;charset=UTF-8"
    }
    
    class Extra:
        ...