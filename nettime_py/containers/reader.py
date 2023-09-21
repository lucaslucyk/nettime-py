from .base import ContainerBase
from ..schemas.readers import Reader as ReaderSchema


class Reader(ContainerBase[ReaderSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Lector"
    list_schema = ReaderSchema