from datetime import date, timedelta

import pytest
from pydantic import ValidationError

from f1_api.domain.race import Race, RaceStatus


def test_race_creation_success() -> None:
    """
    Test that a valid race can be created correctly with default status.
    """
    future_date = date.today() + timedelta(days=30)
    race = Race(name="Monaco Grand Prix", location="Monte Carlo", race_date=future_date)

    assert race.name == "Monaco Grand Prix"
    assert race.location == "Monte Carlo"
    assert race.race_date == future_date
    assert race.status == RaceStatus.SCHEDULED  # Default value check
    assert race.id is not None


def test_race_invalid_status() -> None:
    """
    Test that providing an invalid status string raises a validation error.
    """
    with pytest.raises(ValidationError):
        # The type ignore is needed because Mypy correctly detects this is wrong,
        # but we want to test runtime validation by Pydantic.
        Race(
            name="Italian Grand Prix",
            location="Monza",
            race_date=date.today(),
            status="ONGOING",  # type: ignore
        )
