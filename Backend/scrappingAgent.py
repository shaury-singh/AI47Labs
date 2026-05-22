from bs4 import BeautifulSoup
import requests
import json
from config import return_model_info

def keep_relevant_info(data):
    payload = return_model_info("payload_extract_relevant_info",data)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )
    result = response.json()
    structured_output = result["response"]
    return structured_output

def extract_webpage_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else ""
    paragraphs = soup.find_all("p")
    unique_text = set()
    details = []
    for text in paragraphs:
        if (text.get_text(strip=True) == ""):
            continue
        unique_text.add(text.get_text(strip=True))
    for text in unique_text:
        details.append(text)
    return details

# data = extract_webpage_content("https://www.toddleapp.com/")
# print(keep_relevant_info(data))