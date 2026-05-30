import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("JSON2VIDEOAPI")

def generate_video(images, scene_data, name):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    scenes = []
    counter = 0
    for image in images:
        scenes.append({
            "elements": [
                {
                    "type": "image",
                    "src": image,
                    "duration": scene_data["scenes"][counter]["duration_seconds"]
                },
                {
                    "type": "text",
                    "text": scene_data["scenes"][counter]["on_screen_text"],
                    "position": "center"
                }
            ]
        })
        counter += 1
    payload = {
        "resolution": "1080p",
        "quality": "high",
        "scenes": scenes
    }
    response = requests.post(
        "https://api.json2video.com/v2/movies",
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    print(response.status_code)
    print(response.json())
    project_id = response.json()["project"]
    print("Project ID:", project_id)
    while True:
        status_response = requests.get(
            f"https://api.json2video.com/v2/movies",
            headers=headers
        )
        data = status_response.json()
        print(data)
        break