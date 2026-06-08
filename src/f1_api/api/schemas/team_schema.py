from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TeamCreate(BaseModel):
    """
    Payload received from the client to create a new team.
    """

    name: str = Field(..., min_length=2, max_length=100, examples=["McLaren F1 Team"])
    headquarters: str = Field(
        ..., min_length=2, max_length=100, examples=["Woking, UK"]
    )
    principal: str = Field(
        ..., min_length=2, max_length=100, examples=["Andrea Stella"]
    )


class TeamResponse(TeamCreate):
    """
    Payload returned to the client representing a complete team.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(..., description="Unique identifier for the team")
