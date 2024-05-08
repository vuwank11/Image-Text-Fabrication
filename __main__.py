import argparse
from PIL import Image, ImageDraw, ImageFont
import pathlib
import random
import string
import shutil


def draw_on_mask(img_mask, fontobj):
    draw = ImageDraw.Draw(img_mask)
    text_start_point = (random.randint(0, int(img_mask.size[0]/2)), random.randint(0, int(img_mask.size[1]/2)))

    # Price
    line_1 = "*MRP Rs. " + str(random.randint(100, 1000)) + "/-"
    draw.text(text_start_point, line_1, font=fontobj, fill="black")

    # Date and batch.
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(0, 99)
    alphabets = string.ascii_uppercase
    line_2 = "#" + str(day) + "/" + str(month) + "/" + str(year) + "  " + random.choice(
        alphabets) + " " + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
    draw.text((text_start_point[0], text_start_point[1] + 35), line_2, font=fontobj, fill="black")

    # Volume
    line_3 = "##" + "NET VOL." + str(random.randint(100, 1000)) + "ML"
    draw.text((text_start_point[0], text_start_point[1] + 70), line_3, font=fontobj, fill="black")

    return img_mask


def create_transparent_mask(image, font):
    mask = Image.new("RGBA", image.size, color=(255, 255, 255, 0))
    drawn_mask = draw_on_mask(mask, font)
    mask_rotated = drawn_mask.rotate(random.randint(-10, 10))
    image.alpha_composite(mask_rotated)
    return image


if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument("--image_dir", type=str, required=False, default="./images")
    arg.add_argument("--font_path", type=str, required=False, default="./fonts/inkjet-regular.ttf")
    arg.add_argument("--n", type=str, required=False, default=10)

    args = arg.parse_args()
    args = vars(args)
    n = int(args["n"]) # Arguments are read as strings which must be converted to integer type.
    image_dir = args["image_dir"]
    font_path = args["font_path"]
    output_dir = image_dir + "/output"

    image_dir = pathlib.Path(image_dir)
    font_path = pathlib.Path(font_path)

    font_type = ImageFont.truetype(font=font_path, size=40)
    print("No. of images to be created for each blank image:", n)
    print("Output directory", output_dir)

    shutil.rmtree(output_dir)
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=False)

    for image in image_dir.iterdir():
        for i in range(n):
            if image.is_dir():
                continue

            img = Image.open(image).convert("RGBA")

            new_image = create_transparent_mask(img, font_type)
            new_rgb_image = new_image.convert("RGB") # Convert to RGB to save as jpeg(RGBA cannot be saved as JPEG).
            new_rgb_image.save("images/output/" + image.name.split(".")[0] + "_" + str(i) + ".jpeg")
    print("Image Creation Completed!!!")
