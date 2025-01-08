from openai import OpenAI

client = OpenAI(api_key="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")
import os

# Load OpenAI API key directly for this test
  # Replace with your actual API key

try:
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an English tutor."},
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
    print("Response:", response.choices[0].message.content.strip())
except Exception as e:
    print("Error:", e)
