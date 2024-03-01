# This script overlays a Plasma-colored heatmap image on top of an original image with adjustable transparency and saves the combined image.

import os
from PIL import Image

def go_to_overlay_img(name):
    # Paths to the image files
    curr_path = os.path.dirname(os.path.realpath(__file__))
    plasma_image_path = curr_path + "\\" + name + "_plasma_image.png"
    org_image_path = curr_path + "\\" + name + "_resize.jpg"
    output_image_path = curr_path + "\\" + name + "_combined.png"

    # Load the images
    plasma_image = Image.open(plasma_image_path).convert("RGBA")
    org_image = Image.open(org_image_path).convert("RGBA")

    # Set the transparency of the Plasma image to 60%
    alpha = int(255 * 0.6)
    plasma_image.putalpha(alpha)  # 128 corresponds to 50% transparency

    # Combine the images
    combined_image = Image.alpha_composite(org_image, plasma_image)

    # Save the result
    combined_image.save(output_image_path)
    print("Heatmap for", name, "is successfully saved at:", output_image_path)

