## Sliding Black Box Approach for Explainable Machine Learning Heatmaps

This repository contains scripts for generating heatmaps using the Sliding Black Box (SBB) approach, aimed at enhancing explainability in machine learning models.

### Prerequisites
- Python 3.x
- Required libraries: PIL, numpy, matplotlib, skimage, cv2, scipy

### How to Generate Heatmaps
Follow these steps to generate heatmaps using the SBB approach:

1. Resize Images (resize.py):
   Resize the original images to a standard size to ensure consistency in processing.

2. Create SBB Images (create_sbb_images.py):
   Generate a series of images with a sliding black box mask applied. This step prepares the images for further analysis in the SBB approach.

3. SBB Handler (sbb_handler.py):
   This module manages the entire process of heatmap generation using the SBB approach. It consists of the following sub-modules:

   - Heatmapping (heatmapping.py):
     Perform heatmapping by overlaying the sliding black box images on the original images and extracting relevant features.

   - Create Heatmap (create_heatmap.py):
     Create a composite heatmap from the generated heatmapped images.

   - Scale and Adjust Image (scale_adjust_img.py):
     Scale and adjust the composite heatmap image for better visualization and interpretability.

   - Overlay Image (overlay_img.py):
     Overlay the adjusted heatmap on the original image to visualize the heatmap in context.

### Usage
1. Ensure all required libraries are installed.
2. Run the scripts in the following order:
   - `python resize.py`
   - `python create_sbb_images.py`
   - `python sbb_handler.py`
3. Provide the necessary input parameters such as image name.
4. The output heatmap will be saved as a PNG file in the specified directory.


### Note
- Adjust parameters such as mask size, step size, and sigma value as needed for optimal heatmap generation.
- Ensure that the input images are of sufficient quality and representativeness for accurate heatmap interpretation.
