# This script resizes an image using skimage library, saves it, and imports necessary libraries
from skimage.transform import resize
import os
import matplotlib.image as img

# Get the current path of the script
curr_path = os.path.dirname(os.path.realpath(__file__))

# Define the path to the input image
path = curr_path + "\\See_Sommer.jpg"

# Read the input image
image = img.imread(path)

# Resize the image to dimensions 600x900
image_res = resize(image, (600, 900))

# Save the resized image
img.imsave(curr_path + "\\See_Sommer_resize.jpg", image_res)
