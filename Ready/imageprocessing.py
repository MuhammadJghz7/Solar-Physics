import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu, threshold_mean, threshold_yen, try_all_threshold
from skimage.measure import label, regionprops
from skimage.color import label2rgb
from scipy.io import readsav
from scipy.ndimage import gaussian_filter, laplace, gaussian_laplace
import cv2


conti09 = readsav("D:/Project/Solar Granulation/X9.0 Flare/stksimg_092403.sav")['conti'][10:260, 0:350]
conti15 = readsav("D:/Project/Solar Granulation/X9.0 Flare/stksimg_150406.sav")['conti'][10:260, 0:350]

# Geometrical Analysis - Image Processing
plt.imshow(conti09,origin="lower",cmap="gray")
plt.show()
plt.imshow(conti15,origin="lower",cmap="gray")
plt.show()

a = conti09 > 0.45
b = conti09 * a
penumbra09 = b < 0.75

umbra09 = conti09 < 0.45
plt.imshow(conti09,cmap="gray",origin="lower")
plt.contour(penumbra09,origin="lower",colors="green",alpha=0.7)
plt.contour(umbra09,origin="lower",colors="red",alpha=0.7)
plt.title("Contoured Continuumgram")
plt.axis('off')
plt.show()

labeled_umbra09 = label(umbra09)
labeled_penumbra09 = label(penumbra09)

umbra_props09 = regionprops(labeled_umbra09)
penumbra_props09 = regionprops(labeled_penumbra09)

umbra_areas09 = [prop.area * 49950 for prop in umbra_props09]

penumbra_areas09 = [prop.area * 49950 for prop in penumbra_props09]
plt.plot(penumbra_areas09)
plt.show()
plt.plot(umbra_areas09)
plt.show()
print("Number of umbras : ", len(umbra_areas09))
print("Mean Umbra Area : ", np.sum(umbra_areas09))

print("Number of penumbra : ", len(penumbra_areas09))
print("Mean Penumbra Area : ",penumbra_areas09[12])

a = conti15 > 0.45
b = conti15 * a
penumbra15 = b < 0.75

umbra15 = conti15 < 0.45
plt.imshow(conti15,cmap="gray",origin="lower")
plt.contour(penumbra15,origin="lower",colors="green",alpha=0.7)
plt.contour(umbra15,origin="lower",colors="red",alpha=0.7)
plt.title("Contoured Continuumgram")
plt.axis('off')
plt.show()

labeled_umbra15 = label(umbra15)
labeled_penumbra15 = label(penumbra15)

umbra_props15 = regionprops(labeled_umbra15)
penumbra_props15 = regionprops(labeled_penumbra15)

umbra_areas15 = [prop.area * 49950 for prop in umbra_props15]

penumbra_areas15 = [prop.area * 49950 for prop in penumbra_props15]
plt.plot(penumbra_areas15)
plt.show()
plt.plot(umbra_areas15)
plt.show()
print("Number of umbras : ", len(umbra_areas15))
print("Mean Umbra Area : ", np.sum(umbra_areas15))

print("Number of penumbra : ", len(penumbra_areas15))
print("Mean Penumbra Area : ",penumbra_areas15[13])

print((np.sum(umbra_areas15)/np.sum(umbra_areas09)*100)-100)
print((penumbra_areas09[12]/penumbra_areas15[13]*100)-100)
