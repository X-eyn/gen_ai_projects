import os
from PIL import Image

def resize_and_crop(image_path, output_path, target_width, target_height, maintain_aspect_ratio=True):
    with Image.open(image_path) as img:
        if maintain_aspect_ratio:
           
            img.thumbnail((target_width, target_height), Image.LANCZOS)
        else:
           
            img = img.resize((target_width, target_height), Image.LANCZOS)

       
        left = (img.width - target_width) / 2
        top = (img.height - target_height) / 2
        right = (img.width + target_width) / 2
        bottom = (img.height + target_height) / 2
        cropped_img = img.crop((left, top, right, bottom))
        
        cropped_img.save(output_path)
        print(f"Processed and saved: {output_path}")

def batch_resize_and_crop(input_folder, output_folder, target_width, target_height, maintain_aspect_ratio=True):

    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"processed_{filename}")
            
            resize_and_crop(image_path, output_path, target_width, target_height, maintain_aspect_ratio)


input_folder = "C:/Users/Admin/Downloads/Python OOP/genai_intern_projects/resize_crop_tool/images"  # img inpt
output_folder = "C:/Users/Admin/Downloads/Python OOP/genai_intern_projects/resize_crop_tool/processed_images"  # img outpt
batch_resize_and_crop(input_folder, output_folder, 200, 200, maintain_aspect_ratio=False)
