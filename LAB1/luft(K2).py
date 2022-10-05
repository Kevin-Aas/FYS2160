import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [142.4, 285.6, 417.8, 471.0, 560.5, 698.1, 836.0, 974.4, 1112.5, 1251.4, 1390.1, 1529.7, 1668.8, 1807.7, 1945.5, 2085.5]

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
plt.title("Luft")
plt.legend()
plt.show()