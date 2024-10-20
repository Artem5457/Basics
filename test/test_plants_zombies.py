import pytest
from app.plants_zombies import plants_zombies_battle


@pytest.mark.parametrize(
    "zombies, plants, result",
    [
        ([1, 3, 5, 7], [2, 4, 6, 8], True),
        ([1, 3, 5, 7], [2, 4], False),
        ([1, 3, 5, 7], [2, 4, 0, 8], True),
        ([2, 1, 1, 1], [1, 2, 1, 1], True),
    ]
)
def test_plants_zombies_battle(
    zombies: list[int],
    plants: list[int],
    result: bool
) -> None:
    assert plants_zombies_battle(zombies, plants) == result, (
        f"Function 'plants_zombies_battle' with zombies {
            zombies} and plants {plants} should return {result}"
    )
