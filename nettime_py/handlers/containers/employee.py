from pydantic import validate_call
from .base import ContainerBase
from nettime_py.schemas.containers.list.employees import Employee as ListSchema
from nettime_py.schemas.containers.detail.employees import Employee as DetailSchema
from nettime_py.schemas.containers.detail import Planning


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
