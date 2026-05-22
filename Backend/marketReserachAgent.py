from config import return_model_info
import requests

def market_research(data):
    payload = return_model_info("payload_marketing_hooks",data)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )
    result = response.json()
    return result