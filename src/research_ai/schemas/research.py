from datetime import datetime
from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=5,
        max_length=300
    )
    max_sources: int = Field(
        default=2,
        ge=1,
        le=3
    )


class SourceResult(BaseModel):
    source_name: str
    findings: str


class ResearchReport(BaseModel):
    question: str
    summary: str
    source_results: list[SourceResult]
    elapsed_time: float
    generated_at: datetime
