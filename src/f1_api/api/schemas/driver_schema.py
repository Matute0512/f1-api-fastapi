from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DriverCreate(BaseModel):
    """
    Payload received from the client to create a new driver.
    """

    name: str = Field(..., min_length=2, max_length=100, examples=["Max Verstappen"])
    number: int = Field(
        ..., gt=0, lt=100, description="Driver's racing number (1-99)", examples=[1]
    )
    team_id: UUID = Field(
        ..., description="Identifier of the team the driver races for"
    )


class DriverResponse(DriverCreate):
    """
    Payload returned to the client representing a complete driver.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(..., description="Unique identifier for the driver")
