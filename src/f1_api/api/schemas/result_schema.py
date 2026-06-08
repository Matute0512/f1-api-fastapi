from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class RaceResultCreate(BaseModel):
    """Payload to record a driver's result in a specific race."""

    race_id: UUID = Field(..., description="The ID of the race")
    driver_id: UUID = Field(..., description="The ID of the driver")
    position: int = Field(
        ..., gt=0, description="Finishing position (must be greater than 0)"
    )
    points: float = Field(..., ge=0, description="Points awarded")
    fastest_lap: bool = Field(
        default=False, description="Did the driver set the fastest lap?"
    )


class RaceResultResponse(RaceResultCreate):
    """Payload returned representing a complete race result."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(..., description="Unique identifier for the result")
