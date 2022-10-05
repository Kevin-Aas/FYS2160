import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [150.0, 302.8, 457.3, 604.5, 754.0, 903.3, 1053.1, 1203.6, 1354.5, 1504.5, 1665.5, 1805.5, 1965.5]

n = np.linspace(1, len(data), len(data))
reg = stats.linregress(n, data)

a = reg.slope
b = reg.intercept
delta_a = reg.stderr
L = 1.244
delta_L = 1.5e-3

print(f'Stigningstall:  a = {a:.4} +- {round(delta_a, 1)} [1/s]')

c = 2*L*a
delta_c = c*np.sqrt((delta_a/a)**2 + (delta_L/L)**2)
print(f'Lydhastigheten: c = {c:.4} +- {round(delta_c, 1)} [m/s]')

plt.plot(n, data, 'o', label='original data')
plt.plot(n, reg.intercept + reg.slope*n, 'r--', label='fitted line')
plt.xlabel('Topp nr. [n]')
plt.ylabel('Frekvens [Hz]')
plt.title("Luft T = 70")
plt.legend()
plt.show()