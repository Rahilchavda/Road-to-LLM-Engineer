import time
from typing import List, Optional, Dict, Any
import openai
from ..config import GEMINI_BASE_URL, google_api_key

def chat_completion(
    messages: List[Dict[str, str]],
    model: str = "gemini-2.-flash",
    temperature: float = 0.2,
    max_tokens: int = 1500
) -> str:
    """
    Centralized LLM call used by the entire application.
    Supports retries and model switching.
    """
    model = model or "gemini-2.0-flash"
    if not google_api_key:
        raise ValueError("Google API key is not set. Please set the GOOGLE_API_KEY environment variable.")

    last_error = None

    for attempt in range(3):
        try:
            response = requests.post(
                f"{GEMINI_BASE_URL}/chat/completions",
                headers=headers,
                json=data,
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            last_error = e
            time.sleep(2 ** attempt)
            continue
        except Exception as e:
            last_error = e
            time.sleep(2 ** attempt)
            continue
    raise last_error    
    