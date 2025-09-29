import matplotlib.pyplot as plt
import numpy as np

vertex1 = np.load('core-point_Polynomial.npz')['vertex1']
vertex2 = np.load('core-point_Polynomial.npz')['vertex2']

ny = vertex1.shape[0]
nx = vertex1.shape[1]

# Calc. Doppler LOS velocity
c = 299792.458 # km/s
lambda0_1 = 29.05
lambda0_2 = 75.28
velocities1 = [[0]*nx for _ in range (ny)]
velocities2 = [[0]*nx for _ in range (ny)]
for i in range(0, ny):
    for j in range(0, nx):
        v = (c * ((vertex1[i][j] - lambda0_1) * 0.0215) - 0.00441) / 6301.5
        velocities1[i][j] = v
        v = (c * ((vertex2[i][j] - lambda0_2) * 0.0215) - 0.00693) / 6302.5
        velocities2[i][j] = v