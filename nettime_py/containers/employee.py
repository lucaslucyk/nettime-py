from .base import ContainerBase
from ..schemas.employees import Employee as EmployeeSchema


class Employee(ContainerBase[EmployeeSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Persona"
    schema_class = EmployeeSchema


    @property
    def base_params(self) -> dict:
        return {
            "container": self.container_name,
            "order": self.order
        }