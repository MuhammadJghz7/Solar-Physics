import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu, threshold_mean, threshold_yen, try_all_threshold
from skimage.measure import label, regionprops
from skimage.color import label2rgb
from scipy.io import readsav
from scipy.ndimage import gaussian_filter, laplace, gaussian_laplace
import math


continuum = readsav('D:/istks.sav')['continuum']

# Geometrical Analysis - Image Processing
plt.imshow(continuum,origin="lower",cmap="gray")
plt.show()

laplacian=gaussian_laplace(continuum, sigma=0.948)
thresh=threshold_yen(laplacian)
granules_mask=laplacian<thresh
plt.imshow(continuum,cmap="gray",origin="lower")
plt.contour(granules_mask,origin="lower",colors="red",alpha=0.7)
plt.show()
intergranules_mask = ~granules_mask

labeled_granules = label(granules_mask)
labeled_intergranules = label(intergranules_mask)

granules_props = regionprops(labeled_granules)
intergranules_props = regionprops(labeled_intergranules)

granule_areas = [prop.area * 49950 for prop in granules_props]
granule_areas = granule_areas
pi = [math.pi] * 357
granule_diameters = np.sqrt([x/y for x, y in zip(granule_areas, pi)])*2
granule_perimeters = [prop.perimeter for prop in granules_props]

inter_areas = [prop.area * 49950 for prop in intergranules_props]
inter_areas = inter_areas
inter_perimeters = [prop.perimeter for prop in intergranules_props]

granule_rgb = label2rgb(labeled_granules, bg_label=0)
inter_rgb = label2rgb(labeled_intergranules, bg_label=0)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(granule_rgb, origin='lower')
plt.title("Granules")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(inter_rgb, origin='lower')
plt.title("Intergranules")
plt.axis('off')

plt.tight_layout()
plt.show()

print("Number of granules : ", len(granule_areas))
print("Mean Granule Area : ", np.mean(granule_areas))
print("Mean Granule Perimeter : ", np.mean(granule_perimeters))

print("Number of intergranular lanes : ", len(inter_areas))
print("Mean Inter Granular Area : ", np.mean(inter_areas))
print("Mean Inter Granular Perimeter : ", np.mean(inter_perimeters))

plt.hist(granule_areas, bins=11, color='goldenrod')
plt.title("Histogram of Granule Areas")
plt.xlabel("Granule Area")
plt.ylabel("Number of Occurence")
plt.grid(True)
plt.show()

plt.hist(granule_diameters, bins=15)
plt.show()

plt.scatter(granule_areas, granule_perimeters, alpha=0.6)
plt.title("Granule Perimeters vs. Granule Areas")
plt.xlabel("Granule Areas")
plt.ylabel("Granule Perimeters")
plt.grid(True)
plt.show()

# 3D View
X, Y = np.meshgrid(np.arange(0, 130), np.arange(0, 100))
Z = continuum

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='gray', edgecolor='none')
ax.set_title("Granules & Intergtranular Lanes")
plt.show()