import uvicorn

from app.config.settings import settings

if __name__ == "__main__":
    uvicorn.run("app.app:app", reload=True, port=settings.port, host=settings.host)
