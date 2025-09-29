import numpy as np
from scipy.io import readsav
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from scipy.stats import gaussian_kde
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

norm_stks09 = readsav("D:/Project/Solar Granulation/X9.0 Flare/stks09.sav")['norm_stks']
norm_stks15 = readsav("D:/Project/Solar Granulation/X9.0 Flare/stks15.sav")['norm_stks']
conti09 = readsav("D:/Project/Solar Granulation/X9.0 Flare/stksimg_092403.sav")['conti'][10:260, 0:350]
conti15 = readsav("D:/Project/Solar Granulation/X9.0 Flare/stksimg_150406.sav")['conti'][10:260, 0:350]

x0, x1 = 0, 350
y0, y1 = 10, 250
continuum=readsav("D:/Project/Solar Granulation/X9.0 Flare/stksimg_092403.sav")['conti']
fig, ax = plt.subplots()
ax.imshow(continuum, origin="lower")
plt.title("2024-10-03 09:24:03")
ax.set_yticks([])
ax.set_xticks([])
rect=plt.Rectangle((x0,y0),x1-x0,y1-y0,
                   edgecolor="red",facecolor="none",linewidth=2)
ax.add_patch(rect)
axins=inset_axes(ax, width="60%", height="60%", loc="upper right")
roi=continuum[10:260,0:350]
axins.imshow(roi, origin="lower",cmap="gray")
axins.set_yticks([])
axins.set_xticks([])
mark_inset(ax, axins, loc1=2, loc2=4, fc="none",ec="red",lw=1.5)
plt.show()
continuum=readsav("D:/Project/Solar Granulation/X9.0 Flare/stksimg_150406.sav")['conti']
fig, ax = plt.subplots()
ax.imshow(continuum, origin="lower")
plt.title("2024-10-03 15:04:06")
ax.set_yticks([])
ax.set_xticks([])
rect=plt.Rectangle((x0,y0),x1-x0,y1-y0,
                   edgecolor="red",facecolor="none",linewidth=2)
ax.add_patch(rect)
axins=inset_axes(ax, width="50%", height="50%", loc="upper right")
roi=continuum[10:260,0:350]
axins.imshow(roi, origin="lower",cmap="gray")
axins.set_yticks([])
axins.set_xticks([])
mark_inset(ax, axins, loc1=2, loc2=4, fc="none",ec="red",lw=1.5)
plt.show()

# Brightness Temperature
Conti_Temp09 = np.load('Brightness_Temp.npz')['Conti_Temp09']
Conti_Temp15 = np.load('Brightness_Temp.npz')['Conti_Temp15']

# Visualizing continuum intensity and its temperature
plt.imshow(conti09, cmap='gray', origin='lower')
plt.title("Continuumgram 09:24:03")
plt.axis('off')
plt.tight_layout()
plt.show()
flat_continuum09 = [item for sublist in conti09 for item in sublist]
plt.hist(flat_continuum09, bins=50, edgecolor='black', density=True)
kde = gaussian_kde(flat_continuum09)
x = np.linspace(min(flat_continuum09), max(flat_continuum09), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of Continuums 09:24:03")
plt.xlabel("Continuum Intensity")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()
plt.imshow(Conti_Temp09, cmap='turbo', origin='lower')
plt.title("Brightness Temperature Map - 09:24:03")
plt.colorbar(label='Temperature$_B$ (K)')
plt.axis('off')
plt.tight_layout()
plt.show()
flat_Conti_Temp09 = [item for sublist in Conti_Temp09 for item in sublist]
plt.hist(flat_Conti_Temp09, bins=50, edgecolor='black', density=True)
kde = gaussian_kde(flat_Conti_Temp09)
x = np.linspace(min(flat_Conti_Temp09), max(flat_Conti_Temp09), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of Brightness Temperatures 09:24:03")
plt.xlabel("Temperature (K)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()
plt.imshow(conti15, cmap='gray', origin='lower')
plt.title("Continuumgram 15:04:06")
plt.axis('off')
plt.tight_layout()
plt.show()
flat_continuum15 = [item for sublist in conti15 for item in sublist]
plt.hist(flat_continuum15, bins=50, edgecolor='black', density=True)
kde = gaussian_kde(flat_continuum15)
x = np.linspace(min(flat_continuum15), max(flat_continuum15), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of Continuums 15:04:06")
plt.xlabel("Continuum Intensity")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()
plt.imshow(Conti_Temp15, cmap='turbo', origin='lower')
plt.title("Brightness Temperature Map - 15:04:06")
plt.colorbar(label='Temperature$_B$ (K)')
plt.axis('off')
plt.tight_layout()
plt.show()
flat_Conti_Temp15 = [item for sublist in Conti_Temp15 for item in sublist]
plt.hist(flat_Conti_Temp15, bins=50, edgecolor='black', density=True)
kde = gaussian_kde(flat_Conti_Temp15)
x = np.linspace(min(flat_Conti_Temp15), max(flat_Conti_Temp15), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of Brightness Temperatures 15:04:06")
plt.xlabel("Temperature (K)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()

# Velocity
velocities109 = np.load('Doppler-Velocity09.npz')['velocities1']
velocities209 = np.load('Doppler-Velocity09.npz')['velocities2']
norm = TwoSlopeNorm(vmin=np.min(velocities109), vcenter=0, vmax=np.max(velocities109))
plt.imshow(velocities109, cmap='bwr', origin='lower', norm=norm)
plt.colorbar(label=r"$V_{LOS}$ (km/s)")
plt.title("Line-of-Sight (LOS) Velocity Map (630.15 nm) - 09:24:03")
plt.axis('off')
plt.tight_layout()
plt.show()
norm = TwoSlopeNorm(vmin=np.min(velocities209), vcenter=0, vmax=np.max(velocities209))
plt.imshow(velocities209, cmap='bwr', origin='lower', norm=norm)
plt.colorbar(label=r"$V_{LOS}$ (km/s)")
plt.title("Line-of-Sight (LOS) Velocity Map (630.25 nm) - 09:24:03")
plt.axis('off')
plt.tight_layout()
plt.show()
flat_velocities109 = [item for sublist in velocities109 for item in sublist]
plt.hist(flat_velocities109, bins=75, edgecolor='black', density=True)
kde = gaussian_kde(flat_velocities109)
x = np.linspace(min(flat_velocities109), max(flat_velocities109), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of (LOS) Velocities (630.15 nm) - 09:24:03")
plt.xlabel(r"$V_{LOS}$ (km/s)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()
flat_velocities209 = [item for sublist in velocities209 for item in sublist]
plt.hist(flat_velocities209, bins=75, edgecolor='black', density=True)
kde = gaussian_kde(flat_velocities209)
x = np.linspace(min(flat_velocities209), max(flat_velocities209), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of (LOS) Velocities (630.25 nm) - 09:24:03")
plt.xlabel(r"$V_{LOS}$ (km/s)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()

velocities115 = np.load('Doppler-Velocity15.npz')['velocities1']
velocities215 = np.load('Doppler-Velocity15.npz')['velocities2']
norm = TwoSlopeNorm(vmin=np.min(velocities115), vcenter=0, vmax=np.max(velocities115))
plt.imshow(velocities115, cmap='bwr', origin='lower', norm=norm)
plt.colorbar(label=r"$V_{LOS}$ (km/s)")
plt.title("Line-of-Sight (LOS) Velocity Map (630.15 nm) - 15:04:06")
plt.axis('off')
plt.tight_layout()
plt.show()
norm = TwoSlopeNorm(vmin=np.min(velocities215), vcenter=0, vmax=np.max(velocities215))
plt.imshow(velocities215, cmap='bwr', origin='lower', norm=norm)
plt.colorbar(label=r"$V_{LOS}$ (km/s)")
plt.title("Line-of-Sight (LOS) Velocity Map (630.25 nm) - 15:04:06")
plt.axis('off')
plt.tight_layout()
plt.show()
flat_velocities115 = [item for sublist in velocities115 for item in sublist]
plt.hist(flat_velocities115, bins=55, edgecolor='black', density=True)
kde = gaussian_kde(flat_velocities115)
x = np.linspace(min(flat_velocities115), max(flat_velocities115), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of (LOS) Velocities (630.15 nm) - 15:04:06")
plt.xlabel(r"$V_{LOS}$ (km/s)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()
flat_velocities215 = [item for sublist in velocities215 for item in sublist]
plt.hist(flat_velocities215, bins=55, edgecolor='black', density=True)
kde = gaussian_kde(flat_velocities215)
x = np.linspace(min(flat_velocities215), max(flat_velocities215), 200)
plt.plot(x, kde(x), 'r-')
plt.title("Histogram of (LOS) Velocities (630.25 nm) - 15:04:06")
plt.xlabel(r"$V_{LOS}$ (km/s)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()

# Line Width
width09 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_092403.sav")['width'][10:260, 0:350]
width15 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_150406.sav")['width'][10:260, 0:350]
plt.imshow(width09, origin='lower', norm='log')
plt.title('Doppler Width - 09:24:03')
plt.colorbar(label='Width (d$\\AA$)')
plt.axis('off')
plt.tight_layout()
plt.show()
FWHM = [item for sublist in width09 for item in sublist]
plt.hist(FWHM, bins=50, edgecolor='black', density=True)
kde = gaussian_kde(FWHM)
x = np.linspace(min(FWHM), max(FWHM), 200)
plt.plot(x, kde(x), 'r-')
plt.title(r'Histogram of Doppler Widths - 09:24:03')
plt.xlabel("Doppler Width (d$\\AA$)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()
plt.imshow(width15, origin='lower', norm='log')
plt.title('Doppler Width - 15:04:06')
plt.colorbar(label='Width (d$\\AA$)')
plt.axis('off')
plt.tight_layout()
plt.show()
FWHM = [item for sublist in width15 for item in sublist]
plt.hist(FWHM, bins=75, edgecolor='black', density=True)
kde = gaussian_kde(FWHM)
x = np.linspace(min(FWHM), max(FWHM), 200)
plt.plot(x, kde(x), 'r-')
plt.title(r'Histogram of Doppler Widths - 15:04:06')
plt.xlabel("Doppler Width (d$\\AA$)")
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()

# Line Depth
line_str09 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_092403.sav")['strength'][10:260, 0:350]
line_str15 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_150406.sav")['strength'][10:260, 0:350]
plt.imshow(line_str09, cmap='inferno', origin='lower')
plt.title('Line Strength - 09:24:03')
plt.colorbar(label='Strength')
plt.axis('off')
plt.tight_layout()
plt.show()
depth = [item for sublist in line_str09 for item in sublist]
plt.hist(depth, bins=45, edgecolor='black', density=True)
kde = gaussian_kde(depth)
x = np.linspace(min(depth), max(depth), 200)
plt.plot(x, kde(x), 'r-')
plt.title(r'Histogram of Line Strengths - 09:24:03')
plt.xlabel(r'Line Strength ($I_{continuum}-I_{core}$%)')
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()
plt.imshow(line_str15, cmap='inferno', origin='lower')
plt.title('Line Depth - 15:04:06')
plt.colorbar(label='Strength')
plt.axis('off')
plt.tight_layout()
plt.show()
depth = [item for sublist in line_str15 for item in sublist]
plt.hist(depth, bins=45, edgecolor='black', density=True)
kde = gaussian_kde(depth)
x = np.linspace(min(depth), max(depth), 200)
plt.plot(x, kde(x), 'r-')
plt.title(r'Histogram of Line Strengths - 15:04:06')
plt.xlabel(r'Line Strength ($I_{continuum}-I_{core}$%)')
plt.ylabel("Normalized Number of Occurences")
plt.tight_layout()
plt.show()

# Merlin
flux09 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_092403.sav")['mag_flux'][10:260, 0:350]
norm = TwoSlopeNorm(vmin=flux09.min(), vcenter=0, vmax=flux09.max())
plt.imshow(flux09, origin="lower", cmap="seismic", norm=norm)
plt.title("Magnetic Flux - 09:24:03 (MERLIN)")
plt.axis('off')
plt.tight_layout()
plt.show()
mag_str09 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_092403.sav")['mag_str'][10:260, 0:350]
plt.imshow(mag_str09, origin="lower", cmap="inferno")
plt.title("Magnetic Field Strength - 09:24:03 (MERLIN)")
plt.axis('off')
plt.colorbar(label='|B| (Gauss)')
plt.tight_layout()
plt.show()
mag_str09_flat = [item for sublist in mag_str09[170:220, 165:215] for item in sublist]

flux15 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_150406.sav")['mag_flux'][10:260, 0:350]
norm = TwoSlopeNorm(vmin=flux15.min(), vcenter=0, vmax=flux15.max())
plt.imshow(flux15, origin="lower", cmap="seismic", norm=norm)
plt.title("Magnetic Flux - 15:04:06 (MERLIN)")
plt.axis('off')
plt.tight_layout()
plt.show()
mag_str15 = readsav("D:/Project/Solar Granulation/X9.0 Flare/Merlin_150406.sav")['mag_str'][10:260, 0:350]
plt.imshow(mag_str15, origin="lower", cmap="inferno")
plt.title("Magnetic Field Strength - 15:04:06 (MERLIN)")
plt.axis('off')
plt.colorbar(label='|B| (Gauss)')
plt.tight_layout()
plt.show()
mag_str15_flat = [item for sublist in mag_str15[170:220, 170:220] for item in sublist]

# B Approximation
Bstks09 = np.load('dlambda09.npz')['Bstks']
Bstks15 = np.load('dlambda15.npz')['Bstks']
plt.imshow(Bstks09, origin='lower', cmap='inferno')
plt.colorbar(label="|B| (Gauss)")
plt.title("Mag. Field Approximation (Stokes V) - 09:24:03")
plt.axis('off')
plt.show()
plt.imshow(Bstks15, origin='lower', cmap='inferno')
plt.colorbar(label="|B| (Gauss)")
plt.title("Mag. Field Approximation (Stokes V) - 15:04:06")
plt.axis('off')
plt.show()

# SIR
x0, x1 = 170, 220
y0, y1 = 170, 220
fig, ad = plt.subplots(figsize=(8,6))
ad.imshow(conti09, origin="lower")
plt.title("2024-10-03 09:24:03")
ad.set_yticks([])
ad.set_xticks([])
rect=plt.Rectangle((x0,y0),x1-x0,y1-y0,
                   edgecolor="red",facecolor="none",linewidth=2)
ad.add_patch(rect)
axins=inset_axes(ad, width="50%", height="50%", loc="lower left")
roi=conti09[170:220,170:220]
axins.imshow(roi, origin="lower",cmap="gray")
axins.set_yticks([])
axins.set_xticks([])
plt.title("Selected Region for SIR")
plt.tight_layout()
plt.show()

x = np.arange(0, 2500)
flat_Conti_Temp09 = [item for sublist in Conti_Temp09[170:220, 165:215] for item in sublist]
temp_SIR09 = readsav("sir09.sav")['t']
plt.hist(flat_Conti_Temp09, bins=50, label="Brightness Temperature")
plt.hist(temp_SIR09, alpha=0.5, bins=50, label="Temperature (SIR)")
plt.title("Histogram of SIR Temperatures vs. Brightness Temperatures 09:24:03")
plt.xlabel("T (K)")
plt.ylabel("Number of Occurences")
plt.legend()
plt.show()
B_SIR09 = readsav("sir09.sav")['b']
B_SIR09 = B_SIR09.flatten()
mag_str09_flat = np.array(mag_str09_flat, dtype=np.float32)
plt.hist(mag_str09_flat, bins=40, label="Mag. Field (MERLIN)")
plt.hist(B_SIR09, alpha=0.5, bins=75, label="Mag. Field (SIR)")
plt.title("Histogram of SIR Mag. Field vs. MERLIN Mag. Field - 09:24:03")
plt.xlabel("|B| (Gauss)")
plt.ylabel("Number of Occurences")
plt.legend()
plt.show()
flat_Conti_Temp15 = [item for sublist in Conti_Temp15[170:220, 170:220] for item in sublist]
temp_SIR15 = readsav("sir15.sav")['t']
plt.hist(flat_Conti_Temp15, bins=50, label="Brightness Temperature")
plt.hist(temp_SIR15, alpha=0.5, bins=50, label="Temperature (SIR)")
plt.title("Histogram of SIR Temperatures vs. Brightness Temperatures - 15:04:06")
plt.xlabel("T (K)")
plt.ylabel("Number of Occurences")
plt.legend()
plt.show()
B_SIR15 = readsav("sir15.sav")['b']
B_SIR15 = B_SIR15.flatten()
mag_str15_flat = np.array(mag_str15_flat, dtype=np.float32)
plt.hist(mag_str15_flat, bins=40, label="Mag. Field (MERLIN)")
plt.hist(B_SIR15, alpha=0.5, bins=75, label="Mag. Field (SIR)")
plt.title("Histogram of SIR Mag. Field vs. MERLIN Mag. Field - 15:04:06")
plt.xlabel("|B| (Gauss)")
plt.ylabel("Number of Occurences")
plt.legend()
plt.show()