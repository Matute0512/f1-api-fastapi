from datetime import date
from uuid import UUID

from sqlalchemy import (
    Boolean,
    Date,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy import (
    Enum as SQLEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from f1_api.domain.race import RaceStatus
from f1_api.infra.database import Base


class TeamORM(Base):
    """
    SQLAlchemy ORM model for the 'teams' database table
    """

    __tablename__ = "teams"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    headquarters: Mapped[str] = mapped_column(String(100))
    principal: Mapped[str] = mapped_column(String(100))

    # Relationship: A team can have multiple drivers
    drivers: Mapped[list["DriverORM"]] = relationship(
        back_populates="team", cascade="all, delete-orphan"
    )


class DriverORM(Base):
    """
    SQLAlchemy ORM model for the 'drivers' database table
    """

    __tablename__ = "drivers"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    number: Mapped[int] = mapped_column(Integer, unique=True)

    # Foreign Key linking to the teams table
    team_id: Mapped[UUID] = mapped_column(ForeignKey("teams.id"))

    # Relationship: A driver belongs to one team
    team: Mapped["TeamORM"] = relationship(back_populates="drivers")

    results: Mapped[list["RaceResultORM"]] = relationship(
        back_populates="driver", cascade="all, delete-orphan"
    )


class RaceORM(Base):
    """
    SQLAlchemy ORM model for the 'races' database table.
    """

    __tablename__ = "races"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    location: Mapped[str] = mapped_column(String(100))
    race_date: Mapped[date] = mapped_column(Date)
    status: Mapped[RaceStatus] = mapped_column(
        SQLEnum(RaceStatus), default=RaceStatus.SCHEDULED
    )

    # Relationship: A race has multiple results (one per driver)
    results: Mapped[list["RaceResultORM"]] = relationship(
        back_populates="race", cascade="all, delete-orphan"
    )


class RaceResultORM(Base):
    """
    SQLAlchemy ORM model for the 'race_results' database table.
    """

    __tablename__ = "race_results"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    race_id: Mapped[UUID] = mapped_column(ForeignKey("races.id"))
    driver_id: Mapped[UUID] = mapped_column(ForeignKey("drivers.id"))
    position: Mapped[int] = mapped_column(Integer)
    points: Mapped[float] = mapped_column(Float)
    fastest_lap: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationships mapping back to Race and Driver
    race: Mapped["RaceORM"] = relationship(back_populates="results")
    driver: Mapped["DriverORM"] = relationship(back_populates="results")
