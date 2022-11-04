import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import lammps_logfile

log = lammps_logfile.File("log.lammps")

rho = 0.002

R = 8.3144598   # J/(K*mol)
U = log.get("TotEng")[1:]   # Tar fra 1 siden jeg får en rart stor verdi
T = log.get("Temp")[1:]
P = log.get('Press')[1:]

print(f'****** rho = {rho} ******')

print('-----------')
Z = P / (rho * T)
delta_Z = np.std(Z)
mean_Z = np.mean(Z)
print(f'Z = {mean_Z:.4}')
print(f'delta_Z = {delta_Z:.4}')

reg = linregress(T, U)
a = reg.slope
b = reg.intercept

print('-----------')
c_v = a
delta_c_v = reg.stderr
print(f'c_v = {c_v:.4}')
print(f'delta_c_v = {delta_c_v:.4}')
print('-----------')

f = 2*c_v / R
delta_f = delta_c_v * 2/R       # df/dcv = 2/R
print(f'f = {f:.4}')
print(f'delta_f = {delta_f:.4}')
print('-----------')

plt.plot(T, U, 'o')
plt.plot(T, a*T + b, '--')
plt.xlabel('T [K]')
plt.ylabel('U [J/atom]')
plt.title(f'rho = {rho}')
plt.show()
