from config import config_prompts, return_model_info
import requests
import json


def review_advertisement(prompt):
    payload = {
        "model": "qwen2.5:1.5b",
        "prompt": config_prompts("critic_agent_prompt", prompt),
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.1,
            "num_predict": 400
        }
    }
    response = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )
    result = response.json()
    return json.loads(result["response"])