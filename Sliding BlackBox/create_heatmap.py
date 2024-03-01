# This script reads images from a specified folder, calculates the mean image from a subset of layers,
# and saves the mean image as output.

import cv2
import numpy as np
import os

# Function to read images from a folder and convert them to a NumPy array
def read_images_to_array(folder_path):
    try:
        # Create lists to store images and filenames
        images = []
        file_names = []

        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                # Create full path to the image
                file_path = os.path.join(folder_path, filename)

                # Read image and add it to the list
                img = cv2.imread(file_path)

                # Check if the image was read successfully
                if img is not None:
                    images.append(img)
                    file_names.append(filename)

        # Create a NumPy array where each layer represents an image
        image_array = np.array(images)

        return image_array, file_names

    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Function to calculate the mean image from a subset of layers
def calculate_mean_image(image_array):
    # Calculate mean over the first dimension (axis=0) while ignoring 255 values
    non_max_values = np.ma.masked_equal(image_array[:94], 255)
    mean_image = np.mean(non_max_values, axis=0).astype(np.uint8)
    return mean_image

# Function to save an image
def save_image(image, output_path):
    cv2.imwrite(output_path, image)
    print(f"Image successfully saved at: {output_path}")

# Main function to create a heatmap
def go_to_create_heatmap(name):
    # Determine the current script path
    curr_path = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(curr_path, "heatmap_images")

    # Read images
    image_array, file_names = read_images_to_array(folder_path)

    if image_array is not None:
        print("Images successfully read.")
        print(f"Shape of the NumPy array: {image_array.shape}")

        # Calculate the mean image considering only non-maximum values
        mean_image = calculate_mean_image(image_array)

        # Define output path for the mean image
        output_mean_image_path = os.path.join(curr_path, f"mean_image_{name}_resize.png")

        # Save the mean image
        save_image(mean_image, output_mean_image_path)
    else:
        print("Error while reading images.")
