import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_summary(status):
    try:
        if not API_KEY:
            return "API key missing"

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "HTTP-Referer": "http://localhost",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",  # ✅ FIXED HERE
                "messages": [
                    {
                        "role": "user",
                        "content": f"Give a one-line health summary for an AI agent with status: {status}"
                    }
                ]
            }
        )

        data = response.json()
        print("LLM RESPONSE:", data)

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        return "LLM error"

    except Exception as e:
        print("ERROR:", e)
        return "Summary unavailable"