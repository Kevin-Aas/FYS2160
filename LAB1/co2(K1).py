import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [150.2, 327.3, 432.9, 547.3, 652.0, 760.2, 866.2, 974.8, 1083.0, 1190.7, 1300.2, 1409.1, 1517.1, 1629.9, 1734.5, 1844.2, 1952.2]

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
plt.title("CO2")
plt.legend()
plt.show()