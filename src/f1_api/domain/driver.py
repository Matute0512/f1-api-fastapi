from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class Driver(BaseModel):
    """
    Core domain entity representing a Formula 1 Driver.
    """

    # Use ConfigDict for strict configurations in Pydantic V2
    model_config = ConfigDict(frozen=True)

    id: UUID = Field(
        default_factory=uuid4, description="Unique identifier for the driver"
    )
    name: str = Field(
        ..., min_length=2, max_length=100, description="Driver's full name"
    )
    number: int = Field(..., gt=0, lt=100, description="Driver's racing number (1-99)")
    team_id: UUID = Field(
        ..., description="Identifier of the team the driver races for"
    )
