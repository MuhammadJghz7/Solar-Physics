import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.io import readsav

istks = readsav('D:/istks.sav')['istks']
continuum = readsav('D:/istks.sav')['continuum']

ny = continuum.shape[0]
nx = continuum.shape[1]

# regression - Polynomial
xR1 = [[0]*1 for _ in range(5)]
xR2 = [[0]*1 for _ in range(5)]
p = [[0]*nx for _ in range(ny)]
q = [[0]*nx for _ in range(ny)]
coeff1 = [[0]*nx for _ in range(ny)]
coeff2 = [[0]*nx for _ in range(ny)]
vertex1 = [[0]*nx for _ in range(ny)]
vertex2 = [[0]*nx for _ in range(ny)]
vertex1I = [[0]*nx for _ in range(ny)]
vertex2I = [[0]*nx for _ in range(ny)]
intensity1 = [[0]*nx for _ in range(ny)]
intensity2 = [[0]*nx for _ in range(ny)]
for i in range(0, ny):
    for j in range(0, nx):
        intensity1[i][j] = istks[0:56, i, j]
        intensity2[i][j] = istks[56:112, i, j]
        x1_min = np.argmin(istks[0:56, i, j])
        x2_min = np.argmin(istks[56:112, i, j]) + 56
        xR1 = [x1_min-2, x1_min-1, x1_min, x1_min+1, x1_min+2]
        xR2 = [x2_min-2, x2_min-2, x2_min, x2_min+1, x2_min+2]
        x1_min2 = x1_min - 2
        x1_min3 = x1_min + 3
        x2_min2 = x2_min - 2
        x2_min3 = x2_min + 3
        yR1 = istks[x1_min2:x1_min3, i, j]
        yR2 = istks[x2_min2:x2_min3, i, j]
        coeff1[i][j] = np.polyfit(xR1, yR1, 2)
        coeff2[i][j] = np.polyfit(xR2, yR2, 2)
        a1, b1, c1 = coeff1[i][j]
        a2, b2, c2 = coeff2[i][j]
        p1 = np.poly1d(coeff1[i][j])
        q1 = np.poly1d(coeff2[i][j])
        vertex1[i][j] = p1(-b1/(2*a1))
        vertex2[i][j] = q1(-b2/(2*a2))
        vertex1I[i][j] = -b1/(2*a1)
        vertex2I[i][j] = -b2/(2*a2)
        p[i][j] = p1
        q[i][j] = q1

# Regression - Gaussian
def gaussian(x, a, b, c):
    return (a * np.exp(-(x - b)**2 / (2 * c**2)))
popt1 = [[0]*nx for _ in range(ny)]
popt2 = [[0]*nx for _ in range(ny)]
for i in range(0, ny):
    for j in range(0, nx):
        in_spectrum = (-1 * (istks[0:112, i, j]) + continuum[i][j])
        x1_max = np.argmax(in_spectrum[0:56])
        x2_max = np.argmax(in_spectrum[56:112]) + 56
        xR1 = [x1_max-3, x1_max-2, x1_max-1, x1_max, x1_max+1, x1_max+2, x1_max+3]
        xR2 = [x2_max-3, x2_max-2, x2_max-1, x2_max, x2_max+1, x2_max+2, x2_max+3]
        x1_max3 = x1_max - 3
        x1_max4 = x1_max + 4
        x2_max3 = x2_max - 3
        x2_max4 = x2_max + 4
        yR1 = (in_spectrum[x1_max3:x1_max4])
        yR2 = (in_spectrum[x2_max3:x2_max4])
        a0 = np.max(in_spectrum[0:56])
        b0 = x1_max
        c0 = (56 - 1) / 4
        p0 = [a0, b0, c0]
        popt1[i][j], pcov1 = curve_fit(gaussian, xR1, yR1, p0 = p0)
        a0 = np.max(in_spectrum[56:112])
        b0 = x2_max
        c0 = (112 - 57) / 4
        p0 = [a0, b0, c0]
        popt2[i][j], pcov2 = curve_fit(gaussian, xR2, yR2, p0 = p0)
in_spectrum = (-1 * (istks[0:112, 0, 0]) + continuum[0][0])
plt.scatter(np.arange(0, 112), in_spectrum[0:112])
plt.plot(np.arange(20, 40), gaussian(np.arange(20, 40), *popt1[0][0]))
plt.plot(np.arange(65, 85), gaussian(np.arange(65, 85), *popt2[0][0]))
plt.show()
