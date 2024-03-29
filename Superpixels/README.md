EXML WS23/24 Uni Bonn - Explainable Machine Learinig Seminar: Planet-V2
by Titus Henkelmann, Jakob Weigand and Adrian Weng in February 2024 

-------------------------------------------------------------------------------------------------

The following is a list of all steps, including the associated code, that must be followed to run
the framework "Superpixels". 
All code is done with Python. Do not change folder structure or delete files!

-------------------------------------------------------------------------------------------------

### Prerequisites
- Python 3.x
- Required libraries: numpy, matplotlib, skimage, PIL, cv2

### Usage

* Choose yourself a image that you want to analyze. Insert it in the folder "Superpixels"
	   best with the ending jpg.
* Run the file "Planet_SuperPixel.py". It generates the Superpixels and saves them in a
	   subfolder that will be generated. If needed, the parameters can be adjusted in line 13 to 18. Line 13 needs to be set in each run to your filename, the parameters from line 16-18 can be the inital ones. Results are automatically saved!
* Run the Planet with the images generated in the step before. Fot this, run PlaNet.ipynb in /Network with the function for Superpixels (Cell 4)		
* The results are needed to run "Visualize_Planet_Output.py". Parameters can be set in line 12 and 13 for the current image name(l. 13) and the associated result (l.12)
* All results are stored in your folder "Superpixels". You have an image with the overlapped heatmap, an image with the heatmap only and an image with the colorbar.

