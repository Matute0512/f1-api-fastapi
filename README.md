# F1 API

API REST de datos de Fórmula 1 construida con **FastAPI**, organizada en una arquitectura por capas donde cada capa tiene una única responsabilidad.

## Características

- Endpoints REST para **pilotos**, **carreras**, **equipos** y **resultados**.
- Esquemas Pydantic con validación y serialización tipada.
- Persistencia con **SQLAlchemy** sobre SQLite.
- Migraciones de esquema gestionadas con **Alembic**.
- Script de carga de datos iniciales (`seed_db.py`).
- Suite de tests con casos borde cubiertos.

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-6BA81E?logo=alembic&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)

## Instalación

```bash
poetry install
```

## Configuración

Las variables de entorno se leen desde un archivo `.env` (gitignored). Copiá `.env.example` a `.env` y completá los valores. Nunca versionar credenciales reales.

## Ejecución

```bash
poetry run uvicorn f1_api.main:app --reload
```

La documentación interactiva queda disponible en `/docs`.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Información de la API |
| `POST` | `/drivers/` | Crea un piloto |
| `GET` | `/drivers/{driver_id}` | Obtiene un piloto |
| `POST` | `/races/` | Crea una carrera |
| `GET` | `/races/{race_id}` | Obtiene una carrera |
| `GET` | `/results/{result_id}` | Obtiene un resultado |
| `POST` | `/teams/` | Crea un equipo |
| `GET` | `/teams/{team_id}` | Obtiene un equipo |

## Migraciones

```bash
poetry run alembic upgrade head
poetry run python scripts/seed_db.py   # carga datos iniciales
```

## Estructura

```
src/f1_api/
├── api/
│   ├── routers/          # driver, race, result, team
│   └── schemas/          # DTOs de entrada y salida
├── core/                 # configuracion
├── domain/               # entidades de dominio puras
├── infra/                # database, models, repositories
└── main.py
alembic/versions/         # migraciones de esquema
scripts/seed_db.py        # datos iniciales
tests/                    # tests de dominio e infraestructura
```

## Testing

```bash
poetry run pytest
```

## Licencia

MIT
