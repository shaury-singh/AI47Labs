from config import return_model_info
import requests
import json 

def advertisment_script(data):
    payload = return_model_info("script_writer_prompt",data)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )
    result = response.json()
    structured_output = json.loads(result["response"])
    return structured_output