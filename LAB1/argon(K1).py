import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [174.5, 264.5, 387.7, 521.6, 648.7, 776.2, 904.0, 1030.8, 1159.4, 1290.5, 1417.8, 1546.4, 1675.1, 1804.1, 1933.2, 2061.9, 2191.1]

n = np.linspace(1, len(data), len(data))
reg = stats.linregress(n, data)

a = reg.slope
b = reg.intercept
delta_a = reg.stderr
L = 1.243
delta_L = 1.5e-3

print(f'Stigningstall:  a = {a:.4} +- {round(delta_a, 1)} [1/s]')

c = 2*L*a
delta_c = c*np.sqrt((delta_a/a)**2 + (delta_L/L)**2)
print(f'Lydhastigheten: c = {c:.4} +- {round(delta_c, 1)} [m/s]')

plt.plot(n, data, 'o', label='original data')
plt.plot(n, reg.intercept + reg.slope*n, 'r--', label='fitted line')
plt.xlabel('Topp nr. [n]')
plt.ylabel('Frekvens [Hz]')
plt.title("Argon")
plt.legend()
plt.show()