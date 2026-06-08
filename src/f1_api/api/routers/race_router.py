from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.api.schemas.race_schema import RaceCreate, RaceResponse
from f1_api.domain.race import Race
from f1_api.infra.database import get_db_session
from f1_api.infra.repositories.race_repository import RaceRepository

router = APIRouter(prefix="/races", tags=["races"])


def get_race_repository(
    session: AsyncSession = Depends(get_db_session),
) -> RaceRepository:
    return RaceRepository(session=session)


@router.post("/", response_model=RaceResponse, status_code=status.HTTP_201_CREATED)
async def create_race(
    payload: RaceCreate, repo: RaceRepository = Depends(get_race_repository)
) -> Race:
    new_race = Race(
        name=payload.name,
        location=payload.location,
        race_date=payload.race_date,
        status=payload.status,
    )
    return await repo.create(new_race)


@router.get("/{race_id}", response_model=RaceResponse)
async def get_race(
    race_id: UUID, repo: RaceRepository = Depends(get_race_repository)
) -> Race:
    race = await repo.get_by_id(race_id)
    if not race:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Race not found."
        )
    return race
