from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Instanciamos la aplicación con metadatos útiles para la
# documentación autogenerada (Swagger/Redoc)
app = FastAPI(
    title="F1 REST API",
    description="API profesional de Fórmula 1 para gestión "
    "de datos de carreras y pilotos.",
    version="0.1.0",
)


@app.get("/health", summary="Health Check del sistema")
async def health_check() -> JSONResponse:
    """
    Endpoint de monitoreo básico.
    Devuelve un estado 200 OK y un mensaje indicando que el servicio está activo.
    """
    return JSONResponse(
        content={"status": "ok", "message": "F1 API is running smoothly!"}
    )
