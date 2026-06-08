from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.domain.team import Team
from f1_api.infra.models import TeamORM


class TeamRepository:
    """
    Repository for managing Team domain entities in the database.
    Acts as a translator between Pydantic domain models and SQLAlchemy ORM models.
    """

    def __init__(self, session: AsyncSession) -> None:
        """
        Initializes the repository with a database session.
        """
        self.session = session

    async def create(self, team: Team) -> Team:
        """
        Translate a domain Team to ORM, saves it, and returns the domain model.
        """
        # 1. Translate Domain to ORM
        team_orm = TeamORM(
            id=team.id,
            name=team.name,
            headquarters=team.headquarters,
            principal=team.principal,
        )

        # 2. Save to database
        self.session.add(team_orm)
        await self.session.commit()

        return team

    async def get_by_id(self, team_id: UUID) -> Team | None:
        """
        Fetches a team by ID from the database and translates it back to a domain model.
        """
        # 1. Search in the database
        query = select(TeamORM).where(TeamORM.id == team_id)
        result = await self.session.execute(query)
        team_orm = result.scalar_one_or_none()

        # 2. If not found, return None
        if not team_orm:
            return None

        # 3. Translate ORM back to domain
        return Team(
            id=team_orm.id,
            name=team_orm.name,
            headquarters=team_orm.headquarters,
            principal=team_orm.principal,
        )
