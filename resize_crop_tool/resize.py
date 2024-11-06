import os
from PIL import Image

def resize_and_crop(image_path, target_width, target_height):
    input_dir = os.path.dirname(image_path)
    output_path = os.path.join(input_dir, "output.jpg")
    
    with Image.open(image_path) as img:
        img.thumbnail((target_width, target_height), Image.LANCZOS)
        
        left = (img.width - target_width) / 2
        top = (img.height - target_height) / 2
        right = (img.width + target_width) / 2
        bottom = (img.height + target_height) / 2
        
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
        print(f"Image saved to {output_path}")

resize_and_crop("C:/Users/Admin/Downloads/Python OOP/genai_intern_projects/input.jpg", 800, 800)
