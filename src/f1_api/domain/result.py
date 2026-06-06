from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class RaceResult(BaseModel):
    """
    Core domain entity representing a driver's result in a specific race.
    """

    model_config = ConfigDict(frozen=True)

    id: UUID = Field(
        default_factory=uuid4, description="Unique identifier for the result record"
    )
    race_id: UUID = Field(..., description="Identifier of the race")
    driver_id: UUID = Field(..., description="Identifier of the driver")
    position: int = Field(
        ..., gt=0, description="Finishing position (must be 1 or greater)"
    )
    points: float = Field(
        default=0.0, ge=0.0, description="Championship points awarded"
    )
    fastest_lap: bool = Field(
        default=False, description="Did the driver score the fastest lap?"
    )
