import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

c = [344.0**2, 357.6**2, 368.1**2]
T = [294.35, 318.15, 337.05]

reg = stats.linregress(T, c)
a = reg.slope
b = reg.intercept
delta_a = reg.stderr
x = np.linspace(290, 340, 1000)

print(f'slope = {a}')

plt.plot(T, c, 'o', label='data')
plt.plot(x, reg.intercept + reg.slope*x, 'r--', label='fitted line')
plt.xlabel('Temperatur [K]')
plt.ylabel('c**2')
plt.grid(color='black', linestyle = '--', linewidth = 0.25)
plt.legend()
plt.show()

R = 8.314
M_mol = 28.96e-3
f = 2*R /(a*M_mol - R)
print(f)