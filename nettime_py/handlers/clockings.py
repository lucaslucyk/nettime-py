from datetime import date, timedelta
from typing import TYPE_CHECKING, Any, Generator, Union
from pydantic import TypeAdapter, validate_call
from nettime_py.schemas.clockings import Day, Clocking

if TYPE_CHECKING:
    from nettime_py.api import NetTimeAPI


class Clockings:
    def __init__(self, client: "NetTimeAPI") -> None:
        self._client = client
        self._base_path = "/api/clockings/"

    @property
    def base_url(self) -> str:
        return self._client.url + self._base_path

    @property
    def base_params(self) -> dict:
        return {}

    def _parse_object_as(self, kind: Any, data: Any) -> Any:
        """Parse python object to pydantic model type

        Args:
            kind (Any): Pydantic model type
            data (Any): Python object

        Returns:
            Any: Pydantic model type instance
        """

        return TypeAdapter(kind).validate_python(data)

    @validate_call(
        config={"arbitrary_types_allowed": True},
        validate_return=True,
    )
    def day(
        self,
        employee: int,
        day: Union[date, str],
        **kwargs,
    ) -> Day:
        """Get a day clockings for a given employee

        Args:
            employee (int): Employee id
            day (Union[date, str]): Date to get

        Returns:
            Day: Attendance clocking day
        """

        if not isinstance(day, date):
            day = date.fromisoformat(day)

        params = self.base_params
        params.update(
            {
                "idemp": employee,
                "date": day.isoformat(),
            }
        )

        return self._client.get(url=self.base_url, params=params, **kwargs)

    @staticmethod
    def _date_range(
        start: Union[date, str],
        end: Union[date, str],
    ) -> Generator[date, None, None]:
        """Generate dates between start and end dates

        Args:
            start (Union[date, str]): Start date
            end (Union[date, str]): End date

        Yields:
            Generator[date, None, None]: Each date
        """

        if not isinstance(start, date):
            start = date.fromisoformat(start)
        if not isinstance(end, date):
            end = date.fromisoformat(end)

        for n in range((end - start).days + 1):
            yield start + timedelta(days=n)

    def list(
        self,
        employee: int,
        start: Union[date, str],
        end: Union[date, str],
        **kwargs,
    ) -> Generator[Clocking, Any, None]:
        """Get a list of clockings for an employee between start and end dates

        Args:
            employee (int): Employee id
            start (date): Start date
            end (date): End date

        Yields:
            Generator[Clocking, Any, None]: All clockings between dates
        """

        # for range between start and end dates
        for day in self._date_range(start, end):
            yield from self.day(employee, day, **kwargs).clockings
