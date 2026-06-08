from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.api.schemas.result_schema import RaceResultCreate, RaceResultResponse
from f1_api.domain.result import RaceResult
from f1_api.infra.database import get_db_session
from f1_api.infra.repositories.result_repository import ResultRepository

router = APIRouter(prefix="/results", tags=["Results"])


def get_result_repository(
    session: AsyncSession = Depends(get_db_session),
) -> ResultRepository:
    return ResultRepository(session=session)


@router.post(
    "/", response_model=RaceResultResponse, status_code=status.HTTP_201_CREATED
)
async def create_result(
    payload: RaceResultCreate, repo: ResultRepository = Depends(get_result_repository)
) -> RaceResult:
    new_result = RaceResult(
        race_id=payload.race_id,
        driver_id=payload.driver_id,
        position=payload.position,
        points=payload.points,
        fastest_lap=payload.fastest_lap,
    )
    return await repo.create(new_result)


@router.get("/{result_id}", response_model=RaceResultResponse)
async def get_result(
    result_id: UUID, repo: ResultRepository = Depends(get_result_repository)
) -> RaceResult:
    result = await repo.get_by_id(result_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Result not found."
        )
    return result
