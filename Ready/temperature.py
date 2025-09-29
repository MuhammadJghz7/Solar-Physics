import numpy as np
import matplotlib.pyplot as plt

Conti_Temp1 = np.load('D:/Project/Solar Granulation/Brightness_Temp.npz')['Temp1']
Conti_Temp2 = np.load('D:/Project/Solar Granulation/Brightness_Temp.npz')['Temp2']

ny = Conti_Temp1.shape[0]
nx = Conti_Temp1.shape[1]

plt.imshow(Conti_Temp1, cmap='inferno')
plt.colorbar()
plt.show()

hsra02=6035
hsra06=5540
hsra10=5160
hsra14=4895
hsra18=4720
hsra22=4600

delta_t=Conti_Temp1[:,:]-hsra02

t06=delta_t+hsra06
t10=delta_t+hsra10
t14=delta_t+hsra14
t18=delta_t+hsra18
t22=delta_t+hsra22
Temper1 = [t06, t10, t14, t18, t22]

hsra01=6200
hsra05=5650
hsra09=5240
hsra13=4950
hsra17=4750
hsra21=4630

delta_t=Conti_Temp2[:,:]-hsra01

t05=delta_t+hsra05
t09=delta_t+hsra09
t13=delta_t+hsra13
t17=delta_t+hsra17
t21=delta_t+hsra21
Temper2 = [t05, t09, t13, t17, t21]


popt1 = np.load('D:/Project/Solar Granulation/Gaussian-Fit.npz')['Gaussian1'][:,:,2]
popt2 = np.load('D:/Project/Solar Granulation/Gaussian-Fit.npz')['Gaussian2'][:,:,2]
bis_all = np.load('D:/Project/Solar Granulation/Bisector.npz')['bis_all']
vertex1 = bis_all[0, 4, :, :]
vertex2 = bis_all[1, 0, :, :]

c = 299792458.0 # km/s
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

c = 2.99792458 * 1e8
k_B = 1.380649e-23
h = 6.62607015 * 1e-34
m_p = 1.6726219e-27
m_Fe = 56 * m_p
R = 8.3145

E_turb1 = [[0]*nx for _ in range(ny)]
E_turb2 = [[0]*nx for _ in range(ny)]
E_thermal1 = [[0]*nx for _ in range(ny)]
temper1 = [[0]*nx for _ in range(ny)]
for i in np.arange(0, ny):
    for j in np.arange(0, nx):
        sigma1 = abs(popt1[i][j])
        sigma2 = abs(popt2[i][j])
        
        E_obs = (sigma1 * 0.0215 * 1e-10 * 2 * np.sqrt(2 * np.log(2)) * c) / (630.15 * 1e-9)
        E_thermal = (k_B * Conti_Temp1[i][j]) / m_Fe
        E_turb = np.sqrt(2 * ((E_obs)**2) - (E_thermal))
        E_turb1[i][j] = E_turb
        
        
        E_obs = (sigma2 * 0.0215 * 1e-10 * 2 * np.sqrt(2 * np.log(20)) * c) / (630.25 * 1e-9)
        E_thermal = (k_B * Conti_Temp2[i][j]) / m_Fe
        E_turb = np.sqrt(2 * (E_obs**2) - (E_thermal))
        E_turb2[i][j] = E_turb
        
E_obs = velocities1[0][0]
E_turb = E_turb1[0][0]
E_thermal1[0][0] = ((E_obs)**2) - (((E_turb)**2) / 2)
temper1[0][0]= np.sqrt(E_thermal1[0][0]) * m_Fe / k_B
plt.imshow(E_turb1, cmap='viridis', origin='lower')
plt.title(r'$\xi_{turb}$ (630.15 nm)')
plt.colorbar()
plt.show()
plt.imshow(E_turb2, cmap='viridis', origin='lower')
plt.title(r'$\xi_{turb}$ (630.25 nm)')
plt.colorbar()
plt.show()