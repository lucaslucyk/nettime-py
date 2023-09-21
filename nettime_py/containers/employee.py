from .base import ContainerBase
from ..schemas.elements.employees import Employee as EmployeeSchema


class Employee(ContainerBase[EmployeeSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Persona"
    list_schema = EmployeeSchema