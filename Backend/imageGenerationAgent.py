from huggingface_hub import InferenceClient
from cloudinaryUploader import upload_image
import os
from dotenv import load_dotenv

load_dotenv()

hf_client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_API_KEY"),
)

def build_image_prompts(strategy):
    prompts = []
    for item in strategy['image_prompts']:
        prompt = f"""
        {item['environment']},
        {item['subject_actions']},
        {item['product_interaction']},
        {item['emotional_tone']} atmosphere,
        {item['lighting']},
        {item['camera_composition_style']},
        {item['branding_aesthetic']},
        cinematic commercial photography,
        ultra realistic,
        highly detailed,
        premium social media advertisement,
        shallow depth of field,
        modern educational technology aesthetic,
        emotional storytelling,
        professional ad campaign style
        """
        prompts.append(prompt.strip())
    return prompts


def generate_ad_images(prompts, name):
    generated_images = []
    output_folder = f"Generated_Images/{name}"
    os.makedirs(output_folder, exist_ok=True)
    for i, prompt in enumerate(prompts):
        image = hf_client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )
        output_path = f"Generated_Images/{name}/{name}{i+1}.png"
        image.save(output_path)
        cloud_url = upload_image(output_path)
        generated_images.append(cloud_url)
        # generated_images.append(output_path)
        # print(f"Generated: {output_path}")
        print(f"Uploaded: {cloud_url}")
    return generated_images