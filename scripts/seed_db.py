import asyncio
import sys
import uuid
from datetime import date
from pathlib import Path

from sqlalchemy import delete

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))


async def seed_data() -> None:
    """
    Seeds the SQLite database with initial Formula 1 data for development.
    It cleans up existing rows first to prevent unique or duplicate key constraints.
    """
    from f1_api.domain.race import RaceStatus
    from f1_api.infra.database import async_session_maker
    from f1_api.infra.models import DriverORM, RaceORM, RaceResultORM, TeamORM

    print("Starting database seeding process...")

    async with async_session_maker() as session:
        # Clear existing data to ensure idempotency
        await session.execute(delete(RaceResultORM))
        await session.execute(delete(DriverORM))
        await session.execute(delete(TeamORM))
        await session.execute(delete(RaceORM))

        # 1. Seed Team
        red_bull_id = uuid.uuid4()
        ferrari_id = uuid.uuid4()

        red_bull = TeamORM(
            id=red_bull_id,
            name="Oracle Red Bull Racing",
            headquarters="Milton Keynes, UK",
            principal="Laurent Mekies"
        )
        ferrari = TeamORM(
            id=ferrari_id,
            name="Scuderia Ferrari",
            headquarters="Maranello, Italy",
            principal="Frédéric Vasseur"
        )
        session.add_all([red_bull, ferrari])

        # 2. Seed Drivers
        verstappen_id = uuid.uuid4()
        leclerc_id = uuid.uuid4()

        max_v = DriverORM(
            id=verstappen_id,
            name="Max Verstappen",
            number=1,
            team_id=red_bull_id
        )
        charles_l = DriverORM(
            id=leclerc_id,
            name="Charles Leclerc",
            number=16,
            team_id=ferrari_id
        )

        session.add_all([max_v, charles_l])

        # 3. Seed Races (One Completed and One Scheduled)
        bahrain_race_id = uuid.uuid4()
        monaco_race_id = uuid.uuid4()

        bahrain_gp = RaceORM(
            id=bahrain_race_id,
            name="Bahrain Grand Prix",
            location="Sakhir",
            race_date=date(2026, 3, 2),
            status=RaceStatus.COMPLETED
        )
        monaco_gp = RaceORM(
            id=monaco_race_id,
            name="Monaco Grand Prix",
            location="Monte Carlo",
            race_date=date(2026, 5, 24),
            status=RaceStatus.SCHEDULED
        )
        session.add_all([bahrain_gp, monaco_gp])

        # Commit all changes to SQLite database
        await session.commit()
        print("\n--- IDs GENERADOS PARA PROBAR EN SWAGGER ---")
        print(f"ID Max Verstappen: {verstappen_id}")
        print(f"ID Charles Leclerc: {leclerc_id}")
        print(f"ID Red Bull Racing: {red_bull_id}")
        print("--------------------------------------------\n")
        print("Database successfully seeded with initial F1 records!")

if __name__ == "__main__":
    asyncio.run(seed_data())
