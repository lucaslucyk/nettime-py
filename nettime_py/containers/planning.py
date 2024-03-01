from .base import ContainerBase
from ..schemas.containers.list.planning import Planning as ListSchema
from ..schemas.containers.detail.planning import Planning as DetailSchema


class Planning(ContainerBase[ListSchema, DetailSchema]):
    path_attribute = ""
    order = "id"
    container_name = "IncidenciaFutura"
    list_schema = ListSchema
    detail_schema = DetailSchema
