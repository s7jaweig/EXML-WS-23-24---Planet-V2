## Implementation of the CNN PlaNet

This repository contains scripts for running the convolutional neural network PlaNet. The input loading and output of the network is optimised to run the other scripts of this project, like the sliding box approach, the superpixel approach or to generate the geoplots.

The code runs in JupyterLab. All required files and folder structures are included here and should not be changed.

### Prerequisites
- Python 3.6.9
- JupyterLab
- Required libraries: numpy, tensorflow, tensorflow_hub, matplotlib.image, skimage.transform, pandas, s2spere

### Usage
1. Run the first two cells so load all libraries and functions
2. Copy the folder with the pictures from the different approaches in the `images` folder
4. Fill in the arrays with the image names and further information and run the corresponding cell depending on the approach
   - Cell 3 for sliding box approach
   - Cell 4 for superpixel approach
   - Cell 5 for geoplots
5. Copy the txt-files from the `results` folder and go on with the other steps in the approaches

