import pytest
from pydantic import ValidationError

from f1_api.domain.team import Team


def test_team_creation_success() -> None:
    """
    Test that a valid team can be created correctly.
    """
    team = Team(
        name="Mercedes-AMG Petronas F1 Team",
        headquarters="Brackley, United Kingdom",
        principal="Toto Wolff",
    )

    assert team.name == "Mercedes-AMG Petronas F1 Team"
    assert team.headquarters == "Brackley, United Kingdom"
    assert team.principal == "Toto Wolff"
    assert team.id is not None


def test_team_invalid_name() -> None:
    """
    Test that an extremely short team name raises a validation error.
    """
    with pytest.raises(ValidationError):
        # The minimum length for the name is 2 characters
        Team(name="A", headquarters="Maranello, Italy", principal="Fred Vasseur")
