from fastapi import APIRouter, Query
from typing import Optional
from backend.utils.ai_agent import get_random_word_with_details

word_router = APIRouter()

# In-memory storage for word history
word_history = []
SUPPORTED_SUBJECTS = ["math", "science", "history", "literature", "art", "philosophy", "physics", "biology", "chemistry", "random"]

@word_router.get("/random")
def get_random_word(subject: Optional[str] = Query("random", description="Generate a word for a specific subject")):
    """
    Fetch a random word and its details using AI, optionally filtered by subject.
    """
    try:
        if subject not in SUPPORTED_SUBJECTS:
            return {"error": f"Invalid subject. Supported subjects are: {', '.join(SUPPORTED_SUBJECTS)}"}

        # Pass the subject to the AI agent if it's not 'random'
        subject_prompt = f" in the subject of {subject}" if subject != "random" else ""

        details = get_random_word_with_details(subject_prompt)

        # Check if there was an error from the OpenAI API
        if isinstance(details, dict) and "error" in details:
            return {"error": details["error"]}

        # Extract the word and subject from the details
        word_line = next((line for line in details.split("\n") if line.startswith("- Word:")), None)
        if not word_line:
            raise ValueError("Word details format is invalid.")

        word = word_line.split(":")[1].strip()
        word_history.append({"word": word, "subject": subject, "details": details})

        return {"word": word, "details": details, "subject": subject}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

@word_router.get("/history")
def get_word_history(
    subject: Optional[str] = Query(None, description="Filter by subject/field"),
    sort: Optional[str] = Query("recency", description="Sort by 'recency' (default) or 'alphabetical'")
):
    """
    Retrieve the in-memory history of all generated words, with optional filtering and sorting.
    """
    try:
        filtered_history = word_history

        # Filter by subject if provided
        if subject:
            if subject not in SUPPORTED_SUBJECTS:
                return {"error": f"Invalid subject. Supported subjects are: {', '.join(SUPPORTED_SUBJECTS)}"}
            filtered_history = [word for word in word_history if word["subject"].lower() == subject.lower()]

        # Sort the history
        if sort == "alphabetical":
            filtered_history = sorted(filtered_history, key=lambda x: x["word"])
        elif sort == "recency":
            filtered_history = list(reversed(filtered_history))  # Most recent first

        return {"history": filtered_history}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}