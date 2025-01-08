from openai import OpenAI

client = OpenAI(api_key="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")
import os

# Load OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please set it in your environment variables.")


def get_random_word_with_details():
    """
    Generate a random word and its detailed explanation using OpenAI's updated API.
    """
    try:
        response = client.chat.completions.create(model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are an English tutor. Provide users with random words to learn."},
            {
            "role": "user",
            "content": (
                "You are an English tutor. Your job is to teach users new words."
                "Provide a different random English word each time and explain it.\n"
                "\n- Word:\n"
                "- Prefix:\n"
                "- Suffix:\n"
                "- History:\n"
                "- Origin:\n"
                "- Subject/Field:\n"
                "- Sentence:"
                ),
            },
        ],
        max_tokens=200,
        temperature=0.9)
       
        # Properly access the response message content
        content = response.choices[0].message.content.strip()
        return content
    except Exception as e:
        return {"error": str(e)}
