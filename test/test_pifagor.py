import pytest
from app.pifagor_task import pifagor_pants


@pytest.mark.parametrize(
    "sizes, result",
    [
        ([5, 3, 4], True),
        ([6, 8, 10], True),
        ([0, 4, 8], False),
        ([4, 8, 23, 6], False),
        ([5, 7], False),
    ]
)
def test_is_pifagor_pants(sizes: list[int], result: bool) -> None:
    assert pifagor_pants(sizes) == result, (
        f"Function 'pifagor_pants' with sizes {sizes} should return {result}"
    )
