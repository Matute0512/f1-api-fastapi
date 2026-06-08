from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.api.schemas.driver_schema import DriverCreate, DriverResponse
from f1_api.domain.driver import Driver
from f1_api.infra.database import get_db_session
from f1_api.infra.repositories.driver_repository import DriverRepository

router = APIRouter(prefix="/drivers", tags=["Drivers"])


def get_driver_repository(
    session: AsyncSession = Depends(get_db_session),
) -> DriverRepository:
    """
    Dependency to inject the DriverRepository into the route handlers.
    """
    return DriverRepository(session=session)


@router.post("/", response_model=DriverResponse, status_code=status.HTTP_201_CREATED)
async def create_driver(
    payload: DriverCreate, repo: DriverRepository = Depends(get_driver_repository)
) -> Driver:
    """
    Create a new driver.
    """
    # Create the domain entity.
    # The ID will be automatically generated thanks
    # to the default_factory in the Driver class.
    new_driver = Driver(
        name=payload.name, number=payload.number, team_id=payload.team_id
    )
    return await repo.create(new_driver)


@router.get("/{driver_id}", response_model=DriverResponse)
async def get_driver(
    driver_id: UUID, repo: DriverRepository = Depends(get_driver_repository)
) -> Driver:
    """
    Retrieve a driver by their unique identifier.
    """
    driver = await repo.get_by_id(driver_id)
    if not driver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Driver not found."
        )
    return driver
