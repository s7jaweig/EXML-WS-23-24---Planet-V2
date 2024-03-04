import os
import cv2
import numpy as np
from matplotlib import cm
from PIL import Image
import matplotlib.pyplot as plt


# ====== Hier Variablen setzen ===================


txt_file_name = 'Segmented-Sommer.txt'
img_file_name = 'See_Sommer.jpg'


# ================================================

# Function to import score values from the network output
def importScores(input_txt_path):
    print("importing scores...")
    dateipfad = input_txt_path
    try:
        with open(dateipfad, 'r') as file:
            next(file)
            # Read all columns out of the file
            lines = file.readlines()            

            # Join columns and remove unnecessary symbols
            values_str = ''.join(lines).replace('[', '').replace(']', '').replace('\n', '')
            
            # Convert string to list of floats
            values_list = [float(value) for value in values_str.split()]

            # Return the value list 
            return values_list

    # Catch Exception while import or converting
    except Exception as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        return []  # Return an empty list in case of an error
    

# Import scores
curr_path = os.path.dirname(__file__)
scores = importScores(os.path.join(curr_path, txt_file_name))
print(f'Imported {len(scores)} score values')

# Load labeled Index-Image
results = np.load(os.path.join(curr_path, 'Label_Idx.npy'))
print(f'Shape {results.shape} with min {np.min(results)} and max {np.max(np.max(results))}')

# Set variables for further computations
max_val = np.max(scores)
for i in range(len(scores)):
    scores[i] = (scores[i]/max_val) * 255

print(f'\n\n{scores}')
# Heatmap erstellen
heatmap = np.zeros((results.shape[0], results.shape[1], 3)).astype(np.uint8)
for i in range(heatmap.shape[0]):
    for j in range(heatmap.shape[1]):
        idx = int(results[i, j])-1
        heatmap[i, j, :] = (scores[idx], scores[idx], scores[idx])

# Convert color values to plasma
img_plasma = heatmap.copy()
img_plasma = cm.plasma(img_plasma[:,:,0])
img_plasma = img_plasma[:,:,:3]

# Create plot with heatmap only and colorbar
fig, ax = plt.subplots(figsize=(9, 6))
cax = ax.imshow(img_plasma, cmap='plasma')
# Add Color skalar
cbar = fig.colorbar(cax)
# Label the colorbar with min and max values
cbar.set_label('Activation', rotation=270, labelpad=15)
cbar.ax.get_yaxis().set_ticks([])
for j, lab in enumerate(['Min', 'Max']):
    cbar.ax.text(1, (2 * j + 1) / 4.0, lab, ha='left', va='center', color='white')
plt.show()
plt.imsave(os.path.join(curr_path, "Heatmap_Plasma_" + txt_file_name + '.png'), img_plasma)
fig.savefig(os.path.join(curr_path, "Heatmap_Plasma_CBar" + txt_file_name + '.png'))


# Import both images
img1 = cv2.imread(os.path.join(os.path.dirname(__file__), "Heatmap_Plasma_" + txt_file_name + '.png'), cv2.COLOR_RGB2BGR)
img2 = cv2.imread(os.path.join(os.path.dirname(__file__), img_file_name))

# Convert image to grayscale image
gray_img = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# convert grayscale image to color RGB Image
img2 = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)

# Overlap both images (original image with heatmap)
alpha = 0.5
beta = 1 - alpha
dst = cv2.addWeighted(img1, alpha, img2, beta, 0)

# Save created image
cv2.imwrite(os.path.join(os.path.dirname(__file__), "Overlapped_" + img_file_name), dst)


