from scrappingAgent import extract_webpage_content, keep_relevant_info
from marketReserachAgent import market_research
from creativeStrategyAgent import creative_strategy
from imageGenerationAgent import build_image_prompts, generate_ad_images
from criticAgent import review_advertisement
from movieGeneratorAgent import generate_video
from advertScriptGenerationAgent import advertisment_script
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd

def generateAdvertisment(url,name):
    print(f"\nProcessing: {name}")
    print(f"URL: {url}")
    max_attempts = 3
    attempt = 0
    print(f"attempt: {attempt}")
    data = extract_webpage_content(url)
    print("Data Extraction Complete")
    relevant_data = keep_relevant_info(data)
    print("Relevant Info Extracted")
    marketing_hook = market_research(relevant_data)["response"]
    print("Market Research Completed")
    advert_strategy = advertisment_script(marketing_hook)
    print(advert_strategy)
    strategy = creative_strategy(marketing_hook)
    print("Strategy Made Successfully")
    prompt = build_image_prompts(strategy)
    print("Image Prompt Generated Succesfully")
    review = review_advertisement(prompt)
    print("Review Done SuccessFully")
    while review["score"] < 6 and attempt < max_attempts:
        print("Re Writing The Prompt")
        prompt = build_image_prompts(strategy)
        review = review_advertisement(prompt)
        attempt += 1
    print(review)
    generated_images = generate_ad_images(prompt, name)
    print("Images Generated")
    video_path = generate_video(generated_images, advert_strategy, name)
    print("VIDEO URL:", video_path)
    return {"images": generated_images,
            "video": video_path
    }

def batchProcessCSV(csvFilePath):
    df = pd.read_csv(csvFilePath)
    jobs = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        for index, row in df.iterrows():
            name = row["name"]
            url = row["url"]
            future = executor.submit(generateAdvertisment,url,name)
            jobs.append(future)
        for job in as_completed(jobs):
            try:
                result = job.result()
                print("Completed Job")
            except Exception as e:
                print(f"Job Failed: {e}")
    # for index, row in df.iterrows():
    #     name = row["name"]
    #     url = row["url"]
    #     generateAdvertisment(url,name)

# batchProcessCSV("CSV/url.csv")