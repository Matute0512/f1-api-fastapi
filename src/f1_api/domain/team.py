from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class Team(BaseModel):
    """
    Core domain entity representing a Formula 1 Team (Constructor)
    """

    model_config = ConfigDict(frozen=True)

    id: UUID = Field(
        default_factory=uuid4, description="Unique identifier for the team"
    )
    name: str = Field(
        ..., min_length=2, max_length=100, description="Official team name"
    )
    headquarters: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="City or country of the team's base",
    )
    principal: str = Field(
        ..., min_length=2, max_length=100, description="Team Principal's full name"
    )
