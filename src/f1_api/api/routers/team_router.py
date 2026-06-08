from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.api.schemas.team_schema import TeamCreate, TeamResponse
from f1_api.domain.team import Team
from f1_api.infra.database import get_db_session
from f1_api.infra.repositories.team_repository import TeamRepository

# Create the router for the /teams endpoint
router = APIRouter(prefix="/teams", tags=["teams"])


# Dependency to inject our repository
def get_team_repository(
    session: AsyncSession = Depends(get_db_session),
) -> TeamRepository:
    return TeamRepository(session=session)


@router.post("/", response_model=TeamResponse, status_code=status.HTTP_201_CREATED)
async def create_team(
    payload: TeamCreate, repo: TeamRepository = Depends(get_team_repository)
) -> Team:
    """
    Creates a new Formula 1 Team in the system.
    """
    # 1. Map the web payload to our Domain Model
    new_team = Team(
        name=payload.name,
        headquarters=payload.headquarters,
        principal=payload.principal,
    )

    # 2. Use the repository to save in to the database
    saved_team = await repo.create(new_team)

    return saved_team


@router.get("/{team_id}", response_model=TeamResponse)
async def get_team(
    team_id: UUID, repo: TeamRepository = Depends(get_team_repository)
) -> Team:
    """
    Retrieves a Team by its unique UUID.
    """
    team = await repo.get_by_id(team_id)

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )
    return team
