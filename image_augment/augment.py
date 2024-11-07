import os
from PIL import Image, ImageEnhance, ImageFilter


def augment_image(image_path, output_path, rotate=None, flip=None, scale=None, color_adjust=None, apply_filter=None):

    with Image.open(image_path) as img:

        if rotate is not None:
            img = img.rotate(rotate)
            print(f"Rotated by {rotate} degrees")

        if flip == "horizontal":
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            print("Flipped horizontally")
        elif flip == "vertical":
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            print("Flipped vertically")

        if scale is not None:
            new_size = (int(img.width * scale), int(img.height * scale))
            img = img.resize(new_size, Image.LANCZOS)
            print(f"Scaled by factor {scale}")

        if color_adjust is not None:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(color_adjust)
            print(f"Color adjusted by factor {color_adjust}")

        if apply_filter == "blur":
            img = img.filter(ImageFilter.GaussianBlur(radius=2))
            print("Applied Gaussian blur")
        elif apply_filter == "edge":
            img = img.filter(ImageFilter.FIND_EDGES)
            print("Applied edge detection")
        elif apply_filter == "sharpen":
            img = img.filter(ImageFilter.SHARPEN)
            print("Applied sharpen filter")

        img.save(output_path)
        print(f"Augmented image saved to {output_path}")


def batch_augment_images(input_folder, output_folder, rotate=None, flip=None, scale=None, color_adjust=None, apply_filter=None):

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"augmented_{filename}")

            augment_image(image_path, output_path, rotate, flip,
                          scale, color_adjust, apply_filter)


input_folder = "C:/Users/Admin/Downloads/Python OOP/genai_intern_projects/image_augment/images"
output_folder = "C:/Users/Admin/Downloads/Python OOP/genai_intern_projects/image_augment/augmented_images"

batch_augment_images(input_folder, output_folder, rotate=45,
                     flip="horizontal", scale=1.2, color_adjust=1.5, apply_filter="blur")
#Add more filters
