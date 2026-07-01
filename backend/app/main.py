from fastapi import FastAPI

from app.api.auth.router import router as auth_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI Powered Placement Platform",
    version=settings.VERSION,
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "SkillSync AI Backend Running 🚀",
    }