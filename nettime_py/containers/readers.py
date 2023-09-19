from .container import Container
from ..schemas.readers import Reader as ReaderSchema


class Reader(Container[ReaderSchema]):
    path_attribute = ""
    order = "id"
    container_name = "Lector"
    schema_class = ReaderSchema


    @property
    def base_params(self) -> dict:
        return {
            "container": self.container_name,
            "order": self.order
        }