# Cell 1: Setup
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env from parent directories automatically
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor."},
        {"role": "user", "content": "Explain what an AI agent is in 2 sentences."}
    ]
)

print(response.choices[0].message.content)
print(f"\nTokens used: {response.usage.total_tokens}")