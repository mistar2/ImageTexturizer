from PIL import Image
import random
import sys

# Function to add texture to a solid color image
def add_texture(image_path, variation, dst_img):
    # Load the image
    image = Image.open(image_path)

    # Convert the image to RGB if it's not in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    pixels = image.load()  # Access pixel data

    # Get the image dimensions
    width, height = image.size

    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            # Get the original RGB values
            r, g, b = pixels[x, y]

            # Apply slight variations to each channel
            r = max(0, min(255, r + random.randint(-variation, variation)))
            g = max(0, min(255, g + random.randint(-variation, variation)))
            b = max(0, min(255, b + random.randint(-variation, variation)))

            # Update the pixel with the new values
            pixels[x, y] = (r, g, b)

    # Save the textured image
    new_image_path = dst_img
    image.save(new_image_path)
    return new_image_path

# Example usage

src_img = sys.argv[1]
dst_img = sys.argv[2]
variance = int(sys.argv[3])

textured_image = add_texture(src_img, variance, dst_img)
print(f"Textured image saved at: {textured_image}")
