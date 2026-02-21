"""
Small Langfuse + OpenAI API example.
Based on: https://github.com/langfuse/langfuse-docs/blob/main/cookbook/integration_openai_sdk.ipynb

Uses langfuse.openai as drop-in replacement for openai — traces go to Langfuse.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Drop-in replacement: use langfuse.openai instead of openai
from langfuse.openai import openai

# Optional: use LM Studio (OpenAI-compatible) instead of OpenAI cloud
# Uncomment to use your local LM Studio:
# openai.base_url = os.getenv("LM_STUDIO_BASE_URL")
# openai.api_key = os.getenv("LM_STUDIO_API_KEY")

completion = openai.chat.completions.create(
    name="test-chat",
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
        {"role": "user", "content": "What is 2 + 2? Reply in one word."},
    ],
    temperature=0,
)

response = completion.choices[0].message.content
print(response)
