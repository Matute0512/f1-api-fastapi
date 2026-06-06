from uuid import uuid4

import pytest
from pydantic import ValidationError

from f1_api.domain.result import RaceResult


def test_race_result_creation_success() -> None:
    """
    Test that a valid race result can be created correctly.
    """
    race_id = uuid4()
    driver_id = uuid4()

    result = RaceResult(
        race_id=race_id, driver_id=driver_id, position=1, points=25.0, fastest_lap=True
    )

    assert result.race_id == race_id
    assert result.driver_id == driver_id
    assert result.position == 1
    assert result.points == 25.0
    assert result.fastest_lap is True
    assert result.id is not None


def test_race_result_invalid_position() -> None:
    """
    Test that a finishing position cannot be zero or negative.
    """
    with pytest.raises(ValidationError):
        RaceResult(race_id=uuid4(), driver_id=uuid4(), position=0, points=0.0)


def test_race_result_negative_points() -> None:
    """
    Test that championship points cannot be negative.
    """
    with pytest.raises(ValidationError):
        RaceResult(race_id=uuid4(), driver_id=uuid4(), position=5, points=-10.0)
