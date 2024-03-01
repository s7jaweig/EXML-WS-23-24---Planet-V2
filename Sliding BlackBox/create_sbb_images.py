# This script generates masked images from an input image by creating sliding black boxes of specified dimensions and positions, saving the resulting images in an output folder.

import cv2
import numpy as np
import os

def generate_masked_images(input_image_path, output_folder):
    coord_list = []  # List to store coordinates of black bars
    try:
        # Load input image
        input_image = cv2.imread(input_image_path)

        if input_image is None:
            raise Exception(f"Error loading image from path: {input_image_path}")

        # Get dimensions of input image
        height, width, _ = input_image.shape

        # Define dimensions of black bar
        bar_width = width // 6
        bar_height = height // 4

        # Create output folder if not exists
        os.makedirs(output_folder, exist_ok=True)

        # Generate 96 output images with inverted black bar mask
        for step_col in range(12):
            for step_row in range(8):
                # Calculate position of black bar based on requirements
                start_col = int(step_col * bar_width / 2)
                start_row = int(step_row * bar_height / 2)

                # Create mask for black bar
                mask = np.zeros((height, width), dtype=np.uint8)
                mask[start_row:start_row + bar_height, start_col:start_col + bar_width] = 255

                # Invert the mask
                inverted_mask = cv2.bitwise_not(mask)

                # Generate output image by applying inverted mask
                output_image = cv2.bitwise_and(input_image, input_image, mask=inverted_mask)

                # Print coordinates and size of black area
                print(f"Step {step_col * 8 + step_row + 1}:")
                print(f"   Top left coordinate: ({start_col}, {start_row})")
                print(f"   Width: {bar_width}, Height: {bar_height}")
                coord_list.append((start_col, start_row))

                step = (((step_col * 8) + 1) + (step_row + 1) - 2)

                # Save output image in output folder
                output_path = os.path.join(output_folder, f"See_Sommer_resize_output_{step}.jpg")
                cv2.imwrite(output_path, output_image)
                print("   Image saved as:", output_path)

    except Exception as e:
        print(f"Error: {e}")

    return coord_list, bar_width, bar_height

if __name__ == "__main__":
    # Determine current script path
    curr_path = os.path.dirname(os.path.realpath(__file__))

    # Create paths for input image and output folder
    input_image_path = os.path.join(curr_path, "See_Sommer_resize.jpg")
    output_folder = os.path.join(curr_path, "sbb_images")

    coord_list, bar_width, bar_height = generate_masked_images(input_image_path, output_folder)
    print(coord_list)
    print(bar_width, bar_height)
    #return coord_list, bar_width, bar_height
