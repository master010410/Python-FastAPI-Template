import uvicorn

from app.config.settings import settings
from app.constants import MODE

if __name__ == "__main__":
    uvicorn.run(
        "app.app:app",
        reload=settings.mode == MODE.DEV,
        port=settings.port,
        host=settings.host,
        log_config=settings.logging_config,
    )
