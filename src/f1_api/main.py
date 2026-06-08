from fastapi import FastAPI

from f1_api.api.routers.team_router import router as team_router

app = FastAPI(
    title="F1 REST API",
    description="A Clean Architecture API for Formula 1 Data",
    version="1.0.0",
)

# Connect the Team router
app.include_router(team_router)


@app.get("/")
def health_check() -> dict[str, str]:
    return {"status": "ok", "message": "F1 API is running smoothly!"}
