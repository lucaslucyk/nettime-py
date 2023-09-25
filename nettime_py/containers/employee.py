from .base import ContainerBase
from ..schemas.elements.employees import Employee as ListSchema
from ..schemas.views.employees import Employee as ViewSchema


class Employee(ContainerBase[ListSchema, ViewSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Persona"
    list_schema = ListSchema
    view_schema = ViewSchema