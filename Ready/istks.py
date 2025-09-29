from scipy.io import readsav
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu

stks09 = readsav('D:/Project/Solar Granulation/X9.0 Flare/stks09.sav')['norm_stks']
stks15 = readsav('D:/Project/Solar Granulation/X9.0 Flare/stks15.sav')['norm_stks']
print(stks09.shape)
print(stks15.shape)
plt.imshow(stks09[0,:,:,29])
plt.show()
plt.imshow(stks15[0,:,:,29])
plt.show()

def segment(img):
    thresh = threshold_otsu(img) * 1.08
    mask = img < thresh
    return mask

labels = segment(stks09[0,:,:,0])
plt.imshow(stks09[0,:,:,0], cmap='gray', origin='lower')
plt.contour(labels>0, colors='r', linewidths=0.8)
plt.show()