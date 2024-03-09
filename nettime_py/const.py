from enum import Enum


class ResponseKey(str, Enum):
    TYPE = "type"
    MESSAGE = "message"
    DATA_OBJ = "dataObj"
    DATA_OBJECT = "dataObject"
    TASK_COMPLETED = "completed"
    OK = "ok"
    TASK_ID = "taskId"
    ITEMS = "items"


class RequestKey(str, Enum):
    ACTION = "action"
    ALL = "all"
    ELEMENTS = "elements"
    DATA_OBJ = "dataObj"
    TASK_ID = "taskId"
    OFFSET = "pageStartIndex"
    LIMIT = "pageSize"


class ContainerAction(str, Enum):
    DELETE = "Delete"
    COPY = "Copy"
    EDIT_FORM = "editForm"
    VIEW = "View"
    SAVE = "Save"
    SAVE_MASSIVE = "SaveMass"
    ADD_PLANNING = "NewPlanificacion"


class ActionResult(int, Enum):
    SAVE_OK = 6
    SAVE_ERROR = 2
    DELETE_OK = 8
