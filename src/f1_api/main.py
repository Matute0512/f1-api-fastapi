from fastapi import FastAPI
from fastapi.responses import JSONResponse

# We instantiate the application with metadata useful for the
# auto-generated documentation (Swagger/Redoc)
app = FastAPI(
    title="F1 REST API",
    description="API profesional de Fórmula 1 para gestión "
    "de datos de carreras y pilotos.",
    version="0.1.0",
)


@app.get("/health", summary="Health Check del sistema")
async def health_check() -> JSONResponse:
    """
        Basic monitoring endpoint.
    Returns a 200 OK status and a message indicating that the service is active.
    """
    return JSONResponse(
        content={"status": "ok", "message": "F1 API is running smoothly!"}
    )
