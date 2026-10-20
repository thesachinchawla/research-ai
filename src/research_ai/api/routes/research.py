from datetime import datetime, UTC
from time import perf_counter, sleep
import asyncio

from fastapi import APIRouter
from research_ai.schemas.research import ResearchRequest, ResearchReport

router = APIRouter(prefix="/research", tags=["Research"])


@router.post("/create-research", response_model=ResearchReport)
async def create_research(body: ResearchRequest):
    start = perf_counter()
    await asyncio.sleep(1.5)
    return {
        "question": body.question,
        "summary": "This is a summary of the research findings.",
        "source_results": [{"source_name": "sasasa", "findings": "This is a finding from the source."}],
        "elapsed_time": round(perf_counter() - start, 2),
        "generated_at": datetime.now(UTC)
    }
