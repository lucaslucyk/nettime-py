from .base import ContainerBase
from ..schemas.readers import Reader as ReaderSchema


#TODO: create and replace view model
class Reader(ContainerBase[ReaderSchema, ReaderSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Lector"
    list_schema = ReaderSchema
    view_schema = ReaderSchema