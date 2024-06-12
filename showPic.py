from PIL import Image
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.5)  # Adjust for console character aspect ratio
    return image.resize((new_width, new_height))

def add_color_to_blocks(image, width):
    block_str = ""
    pixels = image.convert("RGB").getdata()
    for i, pixel in enumerate(pixels):
        r, g, b = pixel
        color = f"\033[38;2;{r};{g};{b}m"  # Set RGB foreground color
        block_str += color + "█"
        if (i + 1) % width == 0:
            block_str += "\033[0m\n"  # Reset color and add newline
    return block_str

def main(image_path, new_width=10):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    image = resize_image(image, new_width)
    block_str = add_color_to_blocks(image, new_width)
    print(block_str)

if __name__ == '__main__':
    main('pic.jpg')
