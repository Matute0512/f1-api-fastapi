from uuid import uuid4

import pytest
from pydantic import ValidationError

from f1_api.domain.driver import Driver


def test_driver_creation_success() -> None:
    """
    Test that a valid driver can be created correctly
    """
    fake_team_id = uuid4()
    driver = Driver(name="Franco Colapinto", number=43, team_id=fake_team_id)

    assert driver.name == "Franco Colapinto"
    assert driver.number == 43
    assert driver.id is not None


def test_driver_invalid_number() -> None:
    """
    Test that creating a driver with an invalid number raises an error.
    """
    with pytest.raises(ValidationError):
        # Driver number in F1 must be greater than 0
        Driver(name="Lewis Hamilton", number=0, team_id=uuid4())


def test_driver_is_immutable() -> None:
    """
    Test that domain entities are frozen (immutable).
    """
    driver = Driver(name="Charles Leclerc", number=16, team_id=uuid4())

    with pytest.raises(ValidationError):
        # Trying to mutate a frozen instance should raise an error
        driver.name = "Carlos Sainz"
