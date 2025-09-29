import numpy as np
import scipy
from scipy.io import readsav
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

continuum = readsav('D:/Project/Solar Granulation/X9.0 Flare/stks09.sav')['norm_stks'][0,:,:,:]
continuum = np.mean(continuum[:,:,0:5],2)
# calc. continuum intensity temperature
c = 2.99792458 * 1e8
k_B = 1.380649 * 1e-23
h = 6.62607015 * 1e-34

Conti_Temp09 = [[0]*350 for _ in range(250)]

for i in range(0, 250):
    for j in range(0, 350):   
        Conti_Temp09[i][j] = (h * c) / ((630.15e-9) * k_B * ((np.log(1 + (2 * h * (c**2) / ((630.15e-9)**5 * continuum[i][j] * 2.926e13))))))

# Categorizing
conti = [item for sublist in continuum for item in sublist]
temp = [item for sublist in Conti_Temp09 for item in sublist]

plt.hist(conti, bins=80, edgecolor='black', alpha=0.7)
plt.title('Histogram of continuum intensities')
plt.xlabel("Continuum Intensity")
plt.ylabel("Occurence")
plt.show()

plt.hist(temp, bins=80, edgecolor='black', alpha=0.7)
plt.title('Histogram of temperatures of continuum intensities')
plt.xlabel("Temperature of Continuum Intensity")
plt.ylabel("Occurence")
plt.show()

plt.imshow(Conti_Temp09, cmap='inferno', origin='lower')
plt.colorbar()
plt.show()

Conti_Temp15 = [[0]*350 for _ in range(250)]

continuum = readsav('D:/Project/Solar Granulation/X9.0 Flare/stks15.sav')['norm_stks'][0,:,:,:]
continuum = np.mean(continuum[:,:,0:5],2)
for i in range(0, 250):
    for j in range(0, 350):   
        Conti_Temp15[i][j] = (h * c) / ((630.15e-9) * k_B * ((np.log(1 + (2 * h * (c**2) / ((630.15e-9)**5 * continuum[i][j] * 2.926e13))))))

# Categorizing
conti = [item for sublist in continuum for item in sublist]
temp = [item for sublist in Conti_Temp15 for item in sublist]

plt.hist(conti, bins=80, edgecolor='black', alpha=0.7)
plt.title('Histogram of continuum intensities')
plt.xlabel("Continuum Intensity")
plt.ylabel("Occurence")
plt.show()

plt.hist(temp, bins=80, edgecolor='black', alpha=0.7)
plt.title('Histogram of temperatures of continuum intensities')
plt.xlabel("Temperature of Continuum Intensity")
plt.ylabel("Occurence")
plt.show()

plt.imshow(Conti_Temp15, cmap='inferno', origin='lower')
plt.colorbar()
plt.show()