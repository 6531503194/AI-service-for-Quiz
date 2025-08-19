import getpass, os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base="https://api.openrouter.ai/v1",
)

resp = client.chat.completions.create(
    model="openrouter/gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ]
)

print(resp.choices[0].message.content)
print("Response received successfully.")