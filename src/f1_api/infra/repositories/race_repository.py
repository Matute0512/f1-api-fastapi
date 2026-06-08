from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.domain.race import Race
from f1_api.infra.models import RaceORM


class RaceRepository:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, race: Race) -> Race:
        race_orm = RaceORM(
            id=race.id,
            name=race.name,
            location=race.location,
            race_date=race.race_date,
            status=race.status,
        )
        self.session.add(race_orm)
        await self.session.commit()
        return race

    async def get_by_id(self, race_id: UUID) -> Race | None:
        query = select(RaceORM).where(RaceORM.id == race_id)
        result = await self.session.execute(query)
        race_orm = result.scalar_one_or_none()

        if not race_orm:
            return None

        return Race(
            id=race_orm.id,
            name=race_orm.name,
            location=race_orm.location,
            race_date=race_orm.race_date,
            status=race_orm.status,
        )
