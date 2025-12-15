from pydantic import BaseModel, Field

class MessageRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Input message to summarize")

class SummaryResponse(BaseModel):
    status: str
    summary: str
    timestamp: str
