import numpy as np
import sunpy.map
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from astropy import units as u
from astropy.coordinates import SkyCoord
import warnings
warnings.filterwarnings('ignore')

# SDO - AIA & HMI
data_AIA=sunpy.map.Map("D:/Project/Solar Granulation/X9.0 Flare/Data/SDO/AIA")[0]
data_HMI=sunpy.map.Map("D:/Project/Solar Granulation/X9.0 Flare/Data/SDO/HMI magnetogram")[0]
data_SHARP=sunpy.map.Map("D:/Project/Solar Granulation/X9.0 Flare/Data/SDO/HMI sharp")[5]

aia=data_AIA
bottom_left=SkyCoord(-7*u.arcsec, -410*u.arcsec, frame=aia.coordinate_frame)
top_right=SkyCoord(97*u.arcsec, -329*u.arcsec, frame=aia.coordinate_frame)
submap=aia.submap(bottom_left=bottom_left, top_right=top_right)
submap.plot()
plt.tight_layout()
plt.show()

hmi=data_HMI
submap=hmi.submap(bottom_left=bottom_left, top_right=top_right)
submap.plot_settings['cmap']="hmimag"
submap.plot()
plt.colorbar(label="B (Gauss)")
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.tight_layout()
print(np.min(submap))
print(np.max(submap))
plt.show()

sharp=data_SHARP
print(sharp.meta)
submap=sharp.submap(bottom_left=bottom_left, top_right=top_right)
sd=submap.data
submap.plot_settings['cmap']="gray"
submap.plot()
plt.colorbar(label=r'Mx/$cm^2$')
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()

azi=sunpy.map.Map("D:/Project/Solar Granulation/X9.0 Flare/Data/SDO/HMI sharp")[0]
azi=azi.submap(bottom_left=bottom_left, top_right=top_right)
azi=azi.data
phi=np.deg2rad(azi)
inc=sunpy.map.Map("D:/Project/Solar Granulation/X9.0 Flare/Data/SDO/HMI sharp")[4]
inc=inc.submap(bottom_left=bottom_left, top_right=top_right)
inc=inc.data
gamma=np.deg2rad(inc)

Bx= sd*np.sin(gamma)*np.cos(phi)
By= sd*np.sin(gamma)*np.sin(phi)
Bz= sd*np.cos(gamma)

norm=TwoSlopeNorm(vmin=Bz.min(), vcenter=0, vmax=Bz.max())
plt.imshow(Bz, cmap='bwr', origin='lower', norm=norm)
plt.colorbar(label=r"$B_z$ (Mx/$cm^2$)")
step=5
plt.quiver(np.arange(0, 207, step), np.arange(0, 161, step),
           Bx[::step, ::step], By[::step, ::step],
           color='k', scale=15000)
plt.axis('off')
plt.tight_layout()
plt.show()
