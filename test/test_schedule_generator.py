from datetime import datetime
import pytest
from app.schedule_generator import generate_schedule


@pytest.mark.parametrize(
    "days, work_days, rest_days, start_date, result",
    [
        (5, 2, 1, datetime(2020, 1, 30), [
            datetime(2020, 1, 30, 0, 0),
            datetime(2020, 1, 31, 0, 0),
            datetime(2020, 2, 2, 0, 0),
            datetime(2020, 2, 3, 0, 0)
        ]),
        (7, 2, 3, datetime(2020, 1, 30), [
            datetime(2020, 1, 30, 0, 0),
            datetime(2020, 1, 31, 0, 0),
            datetime(2020, 2, 4, 0, 0),
            datetime(2020, 2, 5, 0, 0),
        ]),
        (4, 2, 1, datetime(2020, 1, 30), [
            datetime(2020, 1, 30, 0, 0),
            datetime(2020, 1, 31, 0, 0),
            datetime(2020, 2, 2, 0, 0),
        ]),
        (3, 3, 0, datetime(2020, 1, 30), [
            datetime(2020, 1, 30, 0, 0),
            datetime(2020, 1, 31, 0, 0),
            datetime(2020, 2, 1, 0, 0),
        ]),
    ]
)
def test_generate_schedule(
    days: int,
    work_days: int,
    rest_days: int,
    start_date: datetime,
    result: list[datetime],
) -> None:
    assert generate_schedule(days, work_days, rest_days, start_date) == result, (
        f"Function 'generate_schedule' should return {result}"
    )
