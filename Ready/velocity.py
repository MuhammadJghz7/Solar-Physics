import matplotlib.pyplot as plt
import numpy as np
from scipy.io import readsav
from matplotlib.colors import TwoSlopeNorm

center = readsav("D:\Project\Solar Granulation\X9.0 Flare\stksimg_092403.sav")['ctrline']
center1 = center[0,10:260,0:350]
center2 = center[1,10:260,0:350]
# Calc. Doppler LOS velocity
c = 299792.458 # km/s
lambda0_1 = 28.5845979
lambda0_2 = 74.9904635946
velocities1 = [[0]*350 for _ in range (250)]
velocities2 = [[0]*350 for _ in range (250)]
for i in range(0, 250):
    for j in range(0, 350):
        v = (c * ((center1[i,j] - lambda0_1) * 0.021549)) / 6301.5
        velocities1[i][j] = v
        v = (c * ((center2[i,j] - lambda0_2) * 0.021549)) / 6302.5
        velocities2[i][j] = v

velocities1_flat = [item for sublist in velocities1 for item in sublist]
velocities2_flat = [item for sublist in velocities2 for item in sublist]
plt.hist(velocities1_flat, bins=50)
plt.show()
plt.hist(velocities2_flat, bins=50)
plt.show()

norm = TwoSlopeNorm(vmin=min(velocities1_flat), vcenter=0, vmax=max(velocities1_flat))
plt.imshow(velocities1, cmap='bwr', norm=norm, origin="lower")
plt.colorbar()
plt.show()
norm = TwoSlopeNorm(vmin=min(velocities2_flat), vcenter=0, vmax=max(velocities2_flat))
plt.imshow(velocities2, cmap='bwr', norm=norm, origin="lower")
plt.colorbar()
plt.show()

#Data 2
center = readsav("D:\Project\Solar Granulation\X9.0 Flare\stksimg_150406.sav")['ctrline']
center1 = center[0,10:260,0:350]
center2 = center[1,10:260,0:350]
velocities2 = [[0]*350 for _ in range (250)]
for i in range(0, 250):
    for j in range(0, 350):
        v = (c * ((center1[i,j] - lambda0_1) * 0.021549)) / 6301.5
        velocities1[i][j] = v
        v = (c * ((center2[i,j] - lambda0_2) * 0.021549)) / 6302.5
        velocities2[i][j] = v

velocities1_flat = [item for sublist in velocities1 for item in sublist]
velocities2_flat = [item for sublist in velocities2 for item in sublist]
plt.hist(velocities1_flat, bins=280)
plt.show()
plt.hist(velocities2_flat, bins=150)
plt.show()

norm = TwoSlopeNorm(vmin=min(velocities1_flat), vcenter=0, vmax=max(velocities1_flat))
plt.imshow(velocities1, cmap='bwr', norm=norm, origin="lower")
plt.colorbar()
plt.show()
norm = TwoSlopeNorm(vmin=min(velocities2_flat), vcenter=0, vmax=max(velocities2_flat))
plt.imshow(velocities2, cmap='bwr', norm=norm, origin="lower")
plt.colorbar()
plt.show()