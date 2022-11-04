import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [158.0, 316.5, 449.5, 591.5, 735.5, 879.5, 1023.4, 1168.8, 1314.7, 1459.5, 1604.5, 1750.5, 1895.5]

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
plt.title("Luft T = 50")
plt.legend()
plt.show()