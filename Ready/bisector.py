import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.io import readsav

istks = readsav('D:/istks.sav')['istks']
continuum = readsav('D:/istks.sav')['continuum']
core1 = np.load("D:/Project/Solar Granulation/core_intensity.npz")['vertex1']
core2 = np.load("D:/Project/Solar Granulation/core_intensity.npz")['vertex2']

ny = istks.shape[1]
nx = istks.shape[2]

# Bisector

inv_istks = np.ndarray([112, ny, nx])
for i in range(ny):
    for j in range(nx):
        inv_istks[:, i, j] = 1 - (istks[:, i, j] / continuum[i, j])
plt.scatter(np.arange(0,112),inv_istks[:, 0, 0])
plt.show()


I = istks

levels = np.array([0.2, 0.4, 0.5, 0.6, 0.75])

def bisector_interp_vec(spectra, levels):
    """
    spectra: shape (n_lambda, ny, nx) 
    levels: لیست نسبی شدت 0..1
    returns: bis_map shape (n_levels, ny, nx)
    """
    n_lambda, ny, nx = spectra.shape
    n_levels = len(levels)
    bis_map = np.zeros((n_levels, ny, nx))
    
    lam_sub = np.arange(n_lambda)  # استفاده از ایندکس به جای طول موج واقعی

    I_max = continuum
    I_min = spectra.min(axis=0)
    I_levels = I_min + levels[:, None, None]*(I_max - I_min)  # shape (n_levels, ny, nx)

    for i, I_level in enumerate(I_levels):
        # سمت چپ
        mask = spectra <= I_level[None, :, :]
        left_idx = mask.argmax(axis=0)
        left_idx_prev = np.maximum(left_idx-1, 0)
        lam_left = lam_sub[left_idx_prev] + (I_level - spectra[left_idx_prev, np.arange(ny)[:,None], np.arange(nx)]) / \
                   (spectra[left_idx, np.arange(ny)[:,None], np.arange(nx)] - spectra[left_idx_prev, np.arange(ny)[:,None], np.arange(nx)]) * \
                   (lam_sub[left_idx] - lam_sub[left_idx_prev])

        # سمت راست
        rev_mask = mask[::-1, :, :]
        right_idx_rev = rev_mask.argmax(axis=0)
        right_idx = n_lambda - 1 - right_idx_rev
        right_idx_next = np.minimum(right_idx+1, n_lambda-1)
        lam_right = lam_sub[right_idx] + (I_level - spectra[right_idx, np.arange(ny)[:,None], np.arange(nx)]) / \
                    (spectra[right_idx_next, np.arange(ny)[:,None], np.arange(nx)] - spectra[right_idx, np.arange(ny)[:,None], np.arange(nx)]) * \
                    (lam_sub[right_idx_next] - lam_sub[right_idx])

        bis_map[i] = (lam_left + lam_right)/2

    return bis_map

# --- دو خط طیفی ---
spec1 = I[20:40, :, :]
spec2 = I[65:85, :, :]

bis_line1 = bisector_interp_vec(spec1, levels)
bis_line2 = bisector_interp_vec(spec2, levels)

# ذخیره در یک آرایه مشترک: (2, 5, ny, nx)
bis_all = np.zeros((2, len(levels), ny, nx))
bis_all[0] = bis_line1
line1 = [[[20 for _ in range(nx)] for _ in range(ny)] for _ in range(5)]
bis_all[0] = [a+b for a,b in zip(bis_all[0],line1)]
bis_all[1] = bis_line2
line2 = [[[65 for _ in range(nx)] for _ in range(ny)] for _ in range(5)]
bis_all[1] = [a+b for a,b in zip(bis_all[1],line2)]

print("Bisectors computed for both lines in bis_all.shape:", bis_all.shape)

 # رسم طیف
x = 89
y = 90
plt.plot(I[:, y, x])

    # رسم نقاط نیمساز
plt.scatter(bis_all[0,:,y,x], core1[y,x] + levels*(continuum[y,x]-core1[y,x]), zorder=5, label="line 1 bisectors")
plt.scatter(bis_all[1,:,y,x], core2[y,x] + levels*(continuum[y,x]-core2[y,x]), zorder=5, label="line 2 bisectors")

plt.xlabel("Wavelength index")
plt.ylabel("Stokes I")
plt.title("Stokes I spectrum and bisectors at pixel ({89},{90})")
plt.axvline(28.5845979, linestyle=':', color='red', label='630.15 nm')
plt.axvline(74.9904635946, linestyle=':', color='red', label='630.25 nm')
plt.legend(loc="lower right", bbox_to_anchor=(1.1, 0))
plt.tight_layout()
plt.show()

continuum = [item for sublist in continuum for item in sublist]

bisector = [item for sublist in bis_all[0,0,:,:] for item in sublist]
plt.scatter(bisector, continuum)
coeffs = np.polyfit(bisector, continuum, 2)
p = np.poly1d(coeffs)
x_fit=np.linspace(27,31,200)
y_fit=p(x_fit)
plt.plot(x_fit, y_fit, color='red')
plt.show()

bisector = [item for sublist in bis_all[0,1,:,:] for item in sublist]
plt.scatter(bisector, continuum)
coeffs = np.polyfit(bisector, continuum, 2)
p = np.poly1d(coeffs)
x_fit=np.linspace(27,31,200)
y_fit=p(x_fit)
plt.plot(x_fit, y_fit, color='red')
plt.show()

bisector = [item for sublist in bis_all[0,2,:,:] for item in sublist]
plt.scatter(bisector, continuum)
coeffs = np.polyfit(bisector, continuum, 2)
p = np.poly1d(coeffs)
x_fit=np.linspace(27,31,200)
y_fit=p(x_fit)
plt.plot(x_fit, y_fit, color='red')
plt.show()

bisector = [item for sublist in bis_all[0,3,:,:] for item in sublist]
plt.scatter(bisector, continuum)
coeffs = np.polyfit(bisector, continuum, 2)
p = np.poly1d(coeffs)
x_fit=np.linspace(27,31,200)
y_fit=p(x_fit)
plt.plot(x_fit, y_fit, color='red')
plt.show()

bisector = [item for sublist in bis_all[0,4,:,:] for item in sublist]
plt.scatter(bisector, continuum)
mask=np.isfinite(bisector)
coeffs = np.polyfit(bisector, continuum, 2)
p = np.poly1d(coeffs)
x_fit=np.linspace(27,31,200)
y_fit=p(x_fit)
plt.plot(x_fit, y_fit, color='red')
plt.show()


bis1=np.mean(bis_all[0,0,:,:])
bis2=np.mean(bis_all[0,1,:,:])
bis3=np.mean(bis_all[0,2,:,:])
bis4=np.mean(bis_all[0,3,:,:])
bis5=np.mean(bis_all[0,4,:,:])
bis=[bis1,bis2,bis3,bis4,bis5]
plt.scatter(bis, levels)
plt.show()