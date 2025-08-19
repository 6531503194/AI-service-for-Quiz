from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("No API key found. Please add OPENROUTER_API_KEY to your .env file.")  

client = OpenAI(
    api_key=API_KEY,
    api_base="https://api.openrouter.ai/v1",
)

def get_openai_analysis(prompt: str, model="openrouter/gpt-4o-mini"):
    """Send prompt to OpenAI and get text response."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content



def get_openai_analysis_with_retry(prompt, retries=5, delay=30, model="openrouter/gpt-4o-mini"):
    for attempt in range(retries):
        try:
            return get_openai_analysis(prompt, model=model)
        except Exception as e:
            print(f"API call failed: {str(e)}. Retrying in {delay} seconds... (Attempt {attempt + 1}/{retries})")
            time.sleep(delay)
    raise Exception("Failed after retries due to API errors")