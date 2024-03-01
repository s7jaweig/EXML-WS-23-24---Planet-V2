# This script orchestrates a series of image processing steps for a given image name.

# Importing functions from separate modules
from heatmapping import go_to_heatmapping
from create_heatmap import go_to_create_heatmap
from scale_adjust_img import go_to_scale_adjust_img
from overlay_img import go_to_overlay_img

# Name of the image
name = "See_Sommer"

# Perform each step of the image processing pipeline
go_to_heatmapping(name)         # Generate heatmap images based on scores
go_to_create_heatmap(name)      # Create a composite heatmap from generated images
go_to_scale_adjust_img(name)    # Scale and adjust the composite heatmap image
go_to_overlay_img(name)         # Overlay the adjusted heatmap on the original image

