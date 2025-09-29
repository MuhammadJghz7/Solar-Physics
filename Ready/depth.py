import numpy as np
from scipy.io import readsav

continuum = readsav('D:/istks.sav')['continuum']
vertex1 = np.load('core_intensity.npz')['vertex1']
vertex2 = np.load('core_intensity.npz')['vertex2']

depth1 = continuum - vertex1
depth2 = continuum - vertex2