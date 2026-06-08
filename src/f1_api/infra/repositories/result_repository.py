from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.domain.result import RaceResult
from f1_api.infra.models import RaceResultORM


class ResultRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, result: RaceResult) -> RaceResult:
        result_orm = RaceResultORM(
            id=result.id,
            race_id=result.race_id,
            driver_id=result.driver_id,
            position=result.position,
            points=result.points,
            fastest_lap=result.fastest_lap,
        )
        self.session.add(result_orm)
        await self.session.commit()
        return result

    async def get_by_id(self, result_id: UUID) -> RaceResult | None:
        query = select(RaceResultORM).where(RaceResultORM.id == result_id)
        result_query = await self.session.execute(query)
        result_orm = result_query.scalar_one_or_none()

        if not result_orm:
            return None

        return RaceResult(
            id=result_orm.id,
            race_id=result_orm.race_id,
            driver_id=result_orm.driver_id,
            position=result_orm.position,
            points=result_orm.points,
            fastest_lap=result_orm.fastest_lap,
        )
