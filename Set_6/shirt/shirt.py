import sys
import os
import requests
from PIL import Image, ImageOps


# define main function
def main():
    shirt, image = get_image()
    overlay_image_with_shirt(shirt, image)

# retrive the two images to overlay
def get_image():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].strip().lower().endswith((".jpg" , ".jpeg" , ".png")):
            if sys.argv[2].strip().lower().endswith((".jpg" , ".jpeg" , ".png")):
                root_ext_1 = os.path.splitext(sys.argv[1].lower())
                root_ext_2 = os.path.splitext(sys.argv[2].lower())
                if root_ext_1[1] == root_ext_2[1]:
                    try:
                        shirt = Image.open(requests.get("https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png", stream=True).raw)
                        image = Image.open(sys.argv[1])
                        return shirt, image
                    except FileNotFoundError:
                        sys.exit("Input does not exist")
                else:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
        else:
            sys.exit("Invalid input")

# overlay the shirt over the given image and save the output
def overlay_image_with_shirt(shirt, image):
    size = shirt.size
    output_image = ImageOps.fit(image, size, method = Image.Resampling.BICUBIC, bleed=0.0, centering=(0, 0.09))
#   shirt.convert("RGBA")
    output_image.paste(shirt, shirt)
    try:
        output_image.save(sys.argv[2])
    except ValueError:
        sys.exit("Output format could not be determined from the file name")
    except OSError:
        sys.exit("The file could not be written")


if __name__ == "__main__":
    main()


