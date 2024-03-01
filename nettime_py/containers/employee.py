from pydantic import validate_call
from .base import ContainerBase
from .schemas.list.employees import Employee as ListSchema
from .schemas.detail.employees import Employee as DetailSchema
from .schemas.detail import Planning


class Employee(ContainerBase[ListSchema, DetailSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Persona"
    list_schema = ListSchema
    detail_schema = DetailSchema

    @validate_call
    def add_planning(
        self, planning: Planning, all_: bool = False, **kwargs
    ) -> Planning:
        if isinstance(planning.employee, list):
            return self._client.plannings.save_massive(
                data=planning, elements=planning.employee, all_=all_, **kwargs
            )
        return self._client.plannings.save(data=planning, **kwargs)
