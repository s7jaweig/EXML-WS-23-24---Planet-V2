# This script generates heatmap images based on scores imported from a text file. 
# It overlays grayscale boxes on a blank white image, mimicking a heatmap effect.

import os
import cv2
import numpy as np

# Function to import scores from a text file
def importScores(input_txt_path):
    print("Importing scores...")
    try:
        with open(input_txt_path, 'r') as file:
            next(file)  # Skip header line
            # Read all lines from the file
            lines = file.readlines()
            # Concatenate the lines and remove unnecessary characters
            values_str = ''.join(lines).replace('[', '').replace(']', '').replace('\n', '')
            # Convert the string to a list of floats
            values_list = [float(value) for value in values_str.split()]
            return values_list

    except Exception as e:
        print(f"Error reading file: {e}")
        return []  # Return an empty list in case of an error

# Function to process grayscale images and generate heatmap images
def process_bw_img(value, index, img_shape, output_path, coord_list, bar_width, bar_height):
    # Invert the score and scale it to the range of 0-255
    value_neg = 100 - (value * 100)
    scaled_value = int(value_neg * 255) // 100
    try:
        # Create a white image
        white_image = np.ones((img_shape[0], img_shape[1], 3), dtype=np.uint8) * 255
        start_col, start_row = coord_list[index]  # Get coordinates for the current bar
        # Overlay the grayscale bar on the white image
        white_image[start_row:start_row + bar_height, start_col:start_col + bar_width, :] = scaled_value
        # Save the resulting image
        cv2.imwrite(output_path, white_image)
        print(f"Image successfully saved at: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Function to iterate through scores and generate heatmap images
def go_to_heatmapping(name):
    curr_path = os.path.dirname(os.path.realpath(__file__))
    # Define paths for input text file and output folder
    txt_file = "Heatmap-" + str(name) + ".txt"
    input_txt_path = os.path.join(curr_path, txt_file)
    score_list = importScores(input_txt_path)
    score_list_len = len(score_list)
    input_path_name = str(name) + "_resize.jpg"
    input_path = os.path.join(curr_path, input_path_name)
    # Define coordinates and dimensions of bars
    coord_list = [(0, 0), (0, 75), ..., (825, 525)]
    bar_width = 150
    bar_height = 150
    # Read input image
    bild = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    img_shape = bild.shape

    # Process each score and generate heatmap images
    for index in range(score_list_len):
        i_name = "sbb_images\\" + str(name) + "_resize_" + str(index) + ".jpg"
        o_name = "heatmap_images\\" + str(name) + "_resize_" + str(index) + ".jpg"
        input_path = os.path.join(curr_path, i_name)
        output_path = os.path.join(curr_path, o_name)
        value = score_list[index]
        process_bw_img(value, index, img_shape, output_path, coord_list, bar_width, bar_height)

