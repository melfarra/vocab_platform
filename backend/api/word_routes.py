from fastapi import APIRouter
from backend.utils.ai_agent import get_random_word_with_details

word_router = APIRouter()

@word_router.get("/random")
def get_random_word():
    """
    Fetch a random word and its details using AI.
    """
    try:
        details = get_random_word_with_details()
        return {"details": details}
    except Exception as e:
        return {"error": str(e)}
