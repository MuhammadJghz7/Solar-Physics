import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.io import readsav

vstks = readsav('D:/Project/Solar Granulation/X9.0 Flare/stks15.sav')['norm_stks'][3,:,:,56:]

# regression - Polynomial
coeff1 = [[0]*350 for _ in range(250)]
coeff2 = [[0]*350 for _ in range(250)]
dlambda = [[0]*350 for _ in range(250)]
vertex1I = [[0]*350 for _ in range(250)]
vertex2I = [[0]*350 for _ in range(250)]
for i in range(0, 250):
    for j in range(0, 350):
        sv = vstks[i, j, :]
        xmax = np.argmax(sv)
        xmin = np.argmin(sv)
        xR1 = [xmax-3, xmax-2, xmax-1, xmax]
        xR2 = [xmin-3, xmin-2, xmin-1, xmin]
        yR1 = [sv[xmax-3], sv[xmax-2], sv[xmax-1], sv[xmax]]
        yR2 = [sv[xmin-3], sv[xmin-2], sv[xmin-1], sv[xmin]]
        coeff1[i][j] = np.polyfit(xR1, yR1, 2)
        coeff2[i][j] = np.polyfit(xR2, yR2, 2)
        a1, b1, c1 = coeff1[i][j]
        a2, b2, c2 = coeff2[i][j]
        vertex1I[i][j] = -b1/(2*a1)
        vertex2I[i][j] = -b2/(2*a2)
        dlambda[i][j] = (vertex1I[i][j] - vertex2I[i][j]) * 0.021549 * 1.07e12 / ((6302.5)**2) / 2.5
Bstks = [[min(max(x, 0), 4000) for x in row] for row in dlambda]
plt.imshow(Bstks, origin='lower', cmap='inferno', vmin=0, vmax=4000)
plt.colorbar()
plt.show()
plt.imshow(Bstks, origin='lower')
plt.show()
Bstks_flat = [item for sublist in Bstks for item in sublist]
plt.hist(Bstks_flat, bins=5)
plt.show()
np.savez('dlambda15.npz', Bstks=Bstks)