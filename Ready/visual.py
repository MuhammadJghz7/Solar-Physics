import numpy as np
from scipy.io import readsav
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

continuum = readsav('D:/Project/Solar Granulation/X9.0 Flare/stks09.sav')['norm_stks'][0,:,:,:]
continuum = np.mean(continuum[:,:,0:5],2)
Merlin = readsav("D:\Project\Solar Granulation\X9.0 Flare\Merlin_092403.sav")
mag_azi = Merlin.mag_azi[10:250, 0:350]
mag_flux = Merlin.mag_flux[10:250, 0:350]
mag_inc = Merlin.mag_inc[10:250, 0:350]
mag_str = Merlin.mag_str[10:250, 0:350]
shift1 = Merlin.shift1[10:250, 0:350]
shift2 = Merlin.shift2[10:250, 0:350]
strength = Merlin.strength[10:250, 0:350]
width = Merlin.width[10:250, 0:350]

plt.imshow(mag_azi, origin="lower", cmap="twilight")
plt.colorbar()
plt.show()
norm = TwoSlopeNorm(vmin=mag_flux.min(), vcenter=0, vmax=mag_flux.max())
plt.imshow(mag_flux, origin="lower", cmap="seismic", norm=norm)
plt.colorbar()
plt.show()
plt.imshow(mag_inc, origin="lower", cmap="cividis")
plt.colorbar()
plt.show()
plt.imshow(mag_str, origin="lower", cmap="inferno")
plt.show()
norm = TwoSlopeNorm(vmin=shift1.min(), vcenter=0, vmax=shift1.max())
plt.imshow(shift1, origin="lower", cmap="seismic", norm=norm)
plt.colorbar()
plt.show()
norm = TwoSlopeNorm(vmin=shift2.min(), vcenter=0, vmax=shift2.max())
plt.imshow(shift2, origin="lower", cmap="seismic", norm=norm)
plt.colorbar()
plt.show()
plt.imshow(strength, origin="lower", cmap="magma")
plt.show()
plt.imshow(width, origin="lower", norm="log")
plt.show()

continuum = readsav('D:/Project/Solar Granulation/X9.0 Flare/stks15.sav')['norm_stks'][0,:,:,:]
continuum = np.mean(continuum[:,:,0:5],2)
Merlin = readsav("D:\Project\Solar Granulation\X9.0 Flare\Merlin_150406.sav")
mag_azi = Merlin.mag_azi[10:250, 0:350]
mag_flux = Merlin.mag_flux[10:250, 0:350]
mag_inc = Merlin.mag_inc[10:250, 0:350]
mag_str = Merlin.mag_str[10:250, 0:350]
shift1 = Merlin.shift1[10:250, 0:350]
shift2 = Merlin.shift2[10:250, 0:350]
strength = Merlin.strength[10:250, 0:350]
width = Merlin.width[10:250, 0:350]

plt.imshow(mag_azi, origin="lower", cmap="twilight")
plt.colorbar()
plt.show()
norm = TwoSlopeNorm(vmin=mag_flux.min(), vcenter=0, vmax=mag_flux.max())
plt.imshow(mag_flux, origin="lower", cmap="seismic", norm=norm)
plt.colorbar()
plt.show()
plt.imshow(mag_inc, origin="lower", cmap="cividis")
plt.colorbar()
plt.show()
plt.imshow(mag_str, origin="lower", cmap="inferno")
plt.show()
norm = TwoSlopeNorm(vmin=shift1.min(), vcenter=0, vmax=shift1.max())
plt.imshow(shift1, origin="lower", cmap="seismic", norm=norm)
plt.colorbar()
plt.show()
norm = TwoSlopeNorm(vmin=shift2.min(), vcenter=0, vmax=shift2.max())
plt.imshow(shift2, origin="lower", cmap="seismic", norm=norm)
plt.colorbar()
plt.show()
plt.imshow(strength, origin="lower", cmap="magma")
plt.show()
plt.imshow(width, origin="lower", norm="log")
plt.show()