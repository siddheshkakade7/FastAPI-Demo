from fastapi import FastAPI, HTTPException
from .schemas import MessageRequest, SummaryResponse
from .services import summarize_message, current_timestamp
from .logger import logger

app = FastAPI(title="FastAPI Demo App")

@app.post("/nevie/test", response_model=SummaryResponse)
def nevie_test(request: MessageRequest):
    try:
        summary = summarize_message(request.message)
        response = SummaryResponse(
            status="ok",
            summary=summary,
            timestamp=current_timestamp()
        )
        logger.info(f"Response: {response.dict()}")
        return response
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
