from .base import ContainerBase
from nettime_py.schemas.containers.list.planning import Planning as ListSchema
from nettime_py.schemas.containers.detail.planning import Planning as DetailSchema


class Planning(ContainerBase[ListSchema, DetailSchema]):
    path_attribute = ""
    order = "id"
    container_name = "IncidenciaFutura"
    list_schema = ListSchema
    detail_schema = DetailSchema
