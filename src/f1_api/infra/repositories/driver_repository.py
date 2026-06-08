from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.domain.driver import Driver
from f1_api.infra.models import DriverORM


class DriverRepository:
    """
    Repository for managing Driver domain entities in the database.
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, driver: Driver) -> Driver:
        """
        Translates a domain Driver to ORM, saves it, and returns the domain model.
        """
        driver_orm = DriverORM(
            id=driver.id,
            name=driver.name,
            number=driver.number,
            team_id=driver.team_id,
        )

        self.session.add(driver_orm)
        await self.session.commit()

        return driver

    async def get_by_id(self, driver_id: UUID) -> Driver | None:
        """
        Fetches a driver by ID and translates it back to a domain model.
        """
        query = select(DriverORM).where(DriverORM.id == driver_id)
        result = await self.session.execute(query)
        driver_orm = result.scalar_one_or_none()

        if not driver_orm:
            return None

        return Driver(
            id=driver_orm.id,
            name=driver_orm.name,
            number=driver_orm.number,
            team_id=driver_orm.team_id,
        )
