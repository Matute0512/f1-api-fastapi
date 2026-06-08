from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from f1_api.domain.race import RaceStatus


class RaceCreate(BaseModel):
    """
    Payload received from the client to create a new race.
    """

    name: str = Field(..., min_length=2, max_length=100, examples=["Monaco Grand Prix"])
    location: str = Field(..., min_length=2, max_length=100, examples=["Monte Carlo"])
    race_date: date = Field(..., examples=["2026-05-24"])
    status: RaceStatus = Field(default=RaceStatus.SCHEDULED)


class RaceResponse(RaceCreate):
    """Payload returned to the client representing a complete race."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(..., description="Unique identifier for the race")
