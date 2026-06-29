from fastapi import FastAPI

app = FastAPI(
    title="SkillSync AI",
    description="AI Powered Placement Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "SkillSync AI Backend Running 🚀"
    }