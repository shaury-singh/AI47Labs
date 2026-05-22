from moviepy import *
import os

def generate_video(images, name):
    clips = []
    for image_path in images:
        clip = (
            ImageClip(image_path)
            .with_duration(3)
            .resized(width=720)
        )
        clips.append(clip)
        final_video = concatenate_videoclips(clips,method="compose")
        output_path = f"Generated_Videos/{name}.mp4"
        os.makedirs("Generated_Videos", exist_ok=True)
        final_video.write_videofile(output_path,fps=24)
        return output_path