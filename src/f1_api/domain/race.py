from datetime import date
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class RaceStatus(str, Enum):
    """
    Allowed statuses for a Formula 1 race.
    """

    SCHEDULED = "SCHEDULED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Race(BaseModel):
    """
    Core domain entity representing a Formula 1 Race (Grand Prix).
    """

    model_config = ConfigDict(frozen=True)

    id: UUID = Field(
        default_factory=uuid4, description="Unique identifier for the race"
    )
    name: str = Field(
        ..., min_length=5, max_length=100, description="Name of the Grand Prix"
    )
    location: str = Field(
        ..., min_length=2, max_length=100, description="City or track location"
    )
    race_date: date = Field(..., description="Date of the main race event")
    status: RaceStatus = Field(
        default=RaceStatus.SCHEDULED, description="Current status of the race"
    )
