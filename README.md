# FastAPI Demo App

A simple FastAPI demo with one endpoint `/nevie/test`.

## Features
- POST endpoint with input validation
- Calls OpenAI (LLM) to summarize a message
- Returns JSON with status, summary, and timestamp
- Console logging in JSON format
- Basic error handling

---
## Project Structure

fastapi-demo/
│
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── schemas.py       # Pydantic models for validation
│   ├── services.py      # LLM call + helper functions
│   └── logger.py        # Logging setup
│
├── requirements.txt     # Dependencies
└── README.md            # Instructions


---

## Setup & Run

1. **Clone or create project folder**
   ```bash
   cd fastapi-demo
2. pip install -r requirements.txt
3. export OPENAI_API_KEY="your_api_key_here"
4. uvicorn app.main:app --reload
5. curl -X POST "http://127.0.0.1:8000/nevie/test" \
-H "Content-Type: application/json" \
-d '{"message":"Hello"}'


## Example Response
{
  "status": "ok",
  "summary": "A greeting message saying hello.",
  "timestamp": "2025-12-15T06:45:12.123456"
}
