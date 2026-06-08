import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from f1_api.domain.team import Team
from f1_api.infra.repositories.team_repository import TeamRepository


@pytest.mark.asyncio
async def test_team_repository_create_and_get(db_session: AsyncSession) -> None:
    """
    Test that a team can be saved to the database and retrieved correctly.
    """
    repository = TeamRepository(session=db_session)

    # 1. Create a domain team in memory
    new_team = Team(
        name="Scuderia Ferrari",
        headquarters="Maranello, Italy",
        principal="Fred Vasseur",
    )

    # 2. Save it using the repository (Translates to ORM and saves to DB)
    saved_team = await repository.create(new_team)

    # 3. Retrieve it by ID from the DB
    fetched_team = await repository.get_by_id(saved_team.id)

    # 4. Verify everything matches perfectly
    assert fetched_team is not None
    assert fetched_team.id == new_team.id
    assert fetched_team.name == "Scuderia Ferrari"
