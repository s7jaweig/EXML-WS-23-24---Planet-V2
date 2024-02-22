import os
import numpy as np
import skimage as ski
import matplotlib.pyplot as plt

'''
Authors: Titus Henkelmann, Jakob Weigand, Adrian Weng
Created for EXML23/24 at University of Bonn
'''

# --------------- Variables need to be set -------------------------

name_of_file = "See_Sommer.jpg"

# --------------- Fixed code, do not change! -----------------------

# Bild einladen
print(f'Loading image {name_of_file} \n   Segmentation in progress...')
img = ski.io.imread(os.path.join(os.path.dirname(__file__), name_of_file))
img = img[:, :, :3]
img = ski.util.img_as_float(img)

# Anzahl der Superpixel, Sigma und Subfolder setzen
num_Segments = 15
sigma = 9
subfolder = 'Segmented_imgs'

# Ordnerstruktur erstellen
subfolder = os.path.join(os.path.dirname(__file__), subfolder)
if os.path.exists(subfolder):
    for file in os.listdir(subfolder):
        os.remove(os.path.join(subfolder, file))
elif not os.path.exists(subfolder):
    os.makedirs(subfolder)
else:
    print(f'Problems while creating subfolder in: {subfolder}')


# Superpixel berechnen und Bilder abspeichern
segments = ski.segmentation.slic(img, n_segments = num_Segments, sigma = sigma)
for seg in range(1, np.max(segments)+1):
    img_seg = np.zeros(img.shape)
    for i in range(segments.shape[0]):
        for j in range(segments.shape[1]):
            if segments[i, j] == seg:
                img_seg[i, j, :] = img[i, j, :]
    if len(str(seg)) == 1:
        str_seg = "00" + str(seg)
    elif len(str(seg)) == 2:
        str_seg = "0" + str(seg)
    else:
        str_seg = str(seg)
    plt.imsave(os.path.join(subfolder, f'Segmented_{str_seg}.png'), img_seg)

print(f'Created {seg} segments and saved them in {subfolder}')

# Label-Indizes abspeichern
np.save(os.path.join(os.path.dirname(__file__), 'Label_Idx.npy'), segments)


# if True:
#     exit()

# Plotten der Ergebnisse
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.imshow(ski.segmentation.mark_boundaries(img, segments))
plt.axis('off')
plt.show()

