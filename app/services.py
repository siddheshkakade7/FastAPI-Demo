import datetime
import os
from openai import OpenAI
from .logger import logger

# Initialize OpenAI client (requires OPENAI_API_KEY env variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_message(message: str) -> str:
    """
    Call OpenAI (or any LLM) to summarize the message.
    """
    try:
        logger.info(f"Summarizing message: {message}")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize this message in one clear sentence."},
                {"role": "user", "content": message},
            ],
            max_tokens=50,
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        logger.error(f"Error calling LLM: {e}")
        raise RuntimeError("LLM summarization failed") from e

def current_timestamp() -> str:
    return datetime.datetime.utcnow().isoformat()
