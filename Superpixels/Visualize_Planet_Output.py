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

# Importfunktion für Scores aus Titus Skript
def importScores(input_txt_path):
    print("importing scores...")
    dateipfad = input_txt_path
    try:
        with open(dateipfad, 'r') as file:
            next(file)
            # Lese alle Zeilen aus der Datei
            lines = file.readlines()            

            # Konkateniere die Zeilen und entferne überflüssige Zeichen
            values_str = ''.join(lines).replace('[', '').replace(']', '').replace('\n', '')
            
            # Konvertiere die Zeichenkette in eine Liste von Floats
            values_list = [float(value) for value in values_str.split()]

            return values_list

    except Exception as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        return []  # Return an empty list in case of an error
    

# Scores einladen
curr_path = os.path.dirname(__file__)
scores = importScores(os.path.join(curr_path, txt_file_name))
print(f'Imported {len(scores)} score values')

# Labeled Index-Bild einladen
results = np.load(os.path.join(curr_path, 'Label_Idx.npy'))
print(f'Shape {results.shape} with min {np.min(results)} and max {np.max(np.max(results))}')

# Variablen für die weitere Berechnung
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

# Konvertieren des Farbschemas nach Plasma
img_plasma = heatmap.copy()
img_plasma = cm.plasma(img_plasma[:,:,0])
img_plasma = img_plasma[:,:,:3]

# Plot erstellen mit reiner Heatmap und seitlicher Colorbar
fig, ax = plt.subplots(figsize=(9, 6))
cax = ax.imshow(img_plasma, cmap='plasma')
# Hinzufügen einer Farbskala
cbar = fig.colorbar(cax)
# Beschriftung der Farbskala mit Min und Max Werten
cbar.set_label('Activation', rotation=270, labelpad=15)
cbar.ax.get_yaxis().set_ticks([])
for j, lab in enumerate(['Min', 'Max']):
    cbar.ax.text(1, (2 * j + 1) / 4.0, lab, ha='left', va='center', color='white')
plt.show()
plt.imsave(os.path.join(curr_path, "Heatmap_Plasma_" + txt_file_name + '.png'), img_plasma)
fig.savefig(os.path.join(curr_path, "Heatmap_Plasma_CBar" + txt_file_name + '.png'))


# Laden Sie die beiden Bilder
img1 = cv2.imread(os.path.join(os.path.dirname(__file__), "Heatmap_Plasma_" + txt_file_name + '.png'), cv2.COLOR_RGB2BGR)
img2 = cv2.imread(os.path.join(os.path.dirname(__file__), img_file_name))

# Konvertieren Sie das RGB-Bild in ein Graustufenbild
gray_img = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# Konvertieren Sie das Graustufenbild in ein RGB-Bild
img2 = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)

# Überlagern Sie die beiden Bilder
alpha = 0.5
beta = 1 - alpha
dst = cv2.addWeighted(img1, alpha, img2, beta, 0)

# Abspeichern der Bilder
cv2.imwrite(os.path.join(os.path.dirname(__file__), "Overlapped_" + img_file_name), dst)
