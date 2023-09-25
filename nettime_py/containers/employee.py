from .base import ContainerBase
from ..schemas.list.employees import Employee as ListSchema
from ..schemas.detail.employees import Employee as DetailSchema


class Employee(ContainerBase[ListSchema, DetailSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Persona"
    list_schema = ListSchema
    detail_schema = DetailSchema
