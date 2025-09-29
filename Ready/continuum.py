import numpy as np
from scipy.io import readsav
import matplotlib.pyplot as plt

continuum = readsav('D:/istks.sav')['continuum']

ny = continuum.shape[0]
nx = continuum.shape[1]
# calc. continuum intensity temperature
c = 2.99792458 * 1e8
k_B = 1.380649 * 1e-23
h = 6.62607015 * 1e-34

Conti_Temp1 = [[0]*nx for _ in range(ny)]
Conti_Temp2 = [[0]*nx for _ in range(ny)]

for i in range(0, ny):
    for j in range(0, nx):   
        Conti_Temp1[i][j] = (h * c) / ((630.15 * 1e-9) * k_B * ((np.log(1 + (2 * h * (c**2) / ((630.15 * 1e-9)**5 * continuum[i][j] * 2.926 * 1e13))))))
        Conti_Temp2[i][j] = (h * c) / ((630.25 * 1e-9) * k_B * ((np.log(1 + (2 * h * (c**2) / ((630.25 * 1e-9)**5 * continuum[i][j] * 2.944 * 1e13))))))