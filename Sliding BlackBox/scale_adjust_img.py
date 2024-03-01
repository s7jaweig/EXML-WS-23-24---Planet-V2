# This script processes grayscale images by scaling their grayscale values, applying Gaussian blur, and converting them to the Plasma colormap.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.ndimage import gaussian_filter
import os

# Function to load the image and scale its grayscale values
def scale_grayscale(image_path):
    # Load the image
    img = Image.open(image_path).convert("L")  # "L" stands for grayscale

    # Scale the grayscale values
    img_array = np.array(img)
    img_scaled = (img_array - img_array.min()) / (img_array.max() - img_array.min()) * 255
    img_scaled = 255 - img_scaled  # Invert the values to make min value white and max value black
    min_val = 100 - ((img_array.min() / 255) * 100)
    max_val = 100 - ((img_array.max() / 255) * 100)
    print(min_val, max_val)

    # Show the scaled image
    plt.imshow(img_scaled, cmap='gray')
    plt.title("Scaled Grayscale Values")
    plt.show()

    return img_scaled, min_val, max_val

# Function to convert the colormap to Plasma with custom color mapping
def convert_to_plasma(img_array, name):
    # Colormap to Plasma with custom color mapping
    custom_plasma = cm.plasma(np.linspace(1, 0, 256))  # Reverse order for color mapping

    img_array_int = img_array.astype(int)  # Convert values to integers

    img_plasma = custom_plasma[img_array_int]

    # Show the image
    plt.imshow(img_plasma)
    plt.title("Colormap to Plasma")
    plt.show()

    # Save the image
    curr_path = os.path.dirname(os.path.realpath(__file__))
    plasma_image = Image.fromarray((img_plasma * 255).astype(np.uint8))
    plasma_image.save(curr_path + "\\" + name + "_plasma_image.png")

    return img_plasma

# Function to apply Gaussian Blur
def apply_gaussian_blur(img_array, sigma=5):
    blurred_img = gaussian_filter(img_array, sigma=sigma)

    # Show the image
    plt.imshow(blurred_img)
    plt.title(f"Gaussian Blur (Sigma={sigma})")
    plt.show()

    return blurred_img

# Main function
def go_to_scale_adjust_img(name):
    # Input is a grayscale image in PNG format
    curr_path = os.path.dirname(os.path.realpath(__file__))
    input_image_path = curr_path + "\\mean_image_" + name + "_resize.png"

    # Scale the grayscale values
    scaled_img, min_val, max_val = scale_grayscale(input_image_path)

    # Apply Gaussian Blur and display
    blur_img = apply_gaussian_blur(scaled_img, sigma=5)

    # Convert to Plasma colormap with custom color mapping and display
    plasma_img = convert_to_plasma(blur_img, name)

    # Add a color scale
    fig, ax = plt.subplots()

    # Display the image
    cax = ax.imshow(plasma_img, cmap='plasma')

    # Add a color bar
    cbar = fig.colorbar(cax)

    # Label the color bar with Min and Max values
    cbar.set_label('Values', rotation=270, labelpad=15)
    cbar.ax.get_yaxis().set_ticks([])
    for j, lab in enumerate(['Min', 'Max']):
        cbar.ax.text(1, (2 * j + 1) / 4.0, lab, ha='left', va='center', color='white')

    plt.show()
