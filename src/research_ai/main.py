from fastapi import FastAPI
from research_ai.api.routes import research_router

app = FastAPI(title="Async Research AI")

app.include_router(research_router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}