from .base import ContainerBase
from ..schemas.containers.list.readers import Reader as ListSchema
from ..schemas.containers.detail.readers import Reader as DetailSchema


# TODO: create and replace view model
class Reader(ContainerBase[ListSchema, DetailSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Lector"
    list_schema = ListSchema
    detail_schema = DetailSchema
