from openai import OpenAI
import os

client = OpenAI(api_key="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")


# Load OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please set it in your environment variables.")


def get_random_word_with_details(subject_prompt: str = ""):
    """
    Generate a random word and its detailed explanation using OpenAI's updated API.
    """
    try:
        response = client.chat.completions.create(model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo"
        messages=[
            {
                    "role": "system",
                    "content": (
                        "You are an English tutor. Provide detailed information about random words."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Give me a random English word{subject_prompt} and explain it in the following format:\n"
                "\n- Word:\n"
                "- Prefix:\n"
                "- Suffix:\n"
                "- History:\n"
                "- Origin:\n"
                "- Subject/Field:\n"
                "- Synonyms:\n"
                "- Antonyms:\n"
                "- Connotation (positive, neutral, or negative):\n"
                "- Denotation (literal meaning):\n"
                "- Example sentence using the word:"
                ),
            },
        ],
        max_tokens=300,
        temperature=1.0,
    )
    # Properly access the response message content
        content = response.choices[0].message.content.strip()
        return content
    except Exception as e:
        return {"error": str(e)}