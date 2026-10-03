import os
import requests

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

def ask_kimi_k3(market_context):
    url = "https://integrate.api.nvidia.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "moonshotai/kimi-k3",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a market-regime classifier. "
                    "Do not place trades. Return concise structured analysis."
                ),
            },
            {
                "role": "user",
                "content": market_context,
            },
        ],
        "temperature": 0.2,
        "max_tokens": 500,
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]