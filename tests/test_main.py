import pytest
from httpx import ASGITransport, AsyncClient

from src.f1_api.main import app


@pytest.mark.asyncio
async def test_health_check() -> None:
    """
    Verifica que el endpoint de health check responda correctamente,
    validando tanto el código de estado HTTP como la estructura del JSON.
    """
    # Configuramos el transporte ASGI para comunicarnos con FastAPI asíncronamente
    transport = ASGITransport(app=app)

    # Usamos AsyncClient de httpx para simular las peticiones
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")

    # Aserciones (Asserts)
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "F1 API is running smoothly!"}
