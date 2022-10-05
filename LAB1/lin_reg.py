import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# [datafrekvenser[Hz], id, lengde på tube[m], temperatur[K], molarmasse [kg/mol]], df:
data_K1_arg = [[174.5, 264.5, 387.7, 521.6, 648.7, 776.2, 904.0, 1030.8, 1159.4, 1290.5, 1417.8, 1546.4, 1675.1, 1804.1, 1933.2, 2061.9, 2191.1], 'K1 - Argon (T=293.75K)', 1.243, 293.75, 39.95e-3, 3]
data_K1_CO2 = [[150.2, 327.3, 432.9, 547.3, 652.0, 760.2, 866.2, 974.8, 1083.0, 1190.7, 1300.2, 1409.1, 1517.1, 1629.9, 1734.5, 1844.2, 1952.2], 'K1 - CO2 (T=293.75K)', 1.243, 293.75, 44.01e-3, 5]
data_K2 = [[142.4, 285.6, 417.8, 471.0, 560.5, 698.1, 836.0, 974.4, 1112.5, 1251.4, 1390.1, 1529.7, 1668.8, 1807.7, 1945.5, 2085.5], 'K2 - Air (T=294.35 K)', 1.244, 294.35, 28.96e-3, 5]
data_K3 = [[150.0, 302.8, 457.3, 604.5, 754.0, 903.3, 1053.1, 1203.6, 1354.5, 1504.5, 1665.5, 1805.5, 1965.5], 'K3 - Air (T=337.05K)', 1.244, 337.05, 28.96e-3, 5]
data_K4 = [[158.0, 316.5, 449.5, 591.5, 735.5, 879.5, 1023.4, 1168.8, 1314.7, 1459.5, 1604.5, 1750.5, 1895.5], 'K4 - Air (T=318.15K)', 1.244, 318.15, 28.96e-3, 5] 

# Legger alt dette i en liste:
data_liste = [data_K1_arg, data_K1_CO2, data_K2, data_K3, data_K4]

for data in data_liste:
    n = np.linspace(1, len(data[0]), len(data[0]))
    reg = stats.linregress(n, data[0])

    a = reg.slope
    b = reg.intercept
    delta_a = reg.stderr
    L = data[2]
    delta_L = 1.5e-3

    print(f'\n-------- {data[1]} --------')
    print(f'Slope:  a = {a:.4} +- {round(delta_a, 1)} [1/s]')
    #print(f'Skjæringspunkt: b = {b:.4}')

    # Eksperimentel lydhastighet:
    c = 2*L*a
    delta_c = c*np.sqrt((delta_a/a)**2 + (delta_L/L)**2)
    print(f'Measured sound velocity: c = {c:.4} +- {round(delta_c, 1)} [m/s]')
    
    # Analytisk lydhastighet med konstant temperatur:
    f = data[5]     # frihetsgrader
    R = 8.314       # J/(mol*K)
    T = data[3]     # K
    M_mol = data[4] # kg/mol
    c_anlytisk = np.sqrt(((f+2)*R*T)/(f*M_mol))
    print(f'Analytic sound velocity: c = {c_anlytisk:.4} [m/s]')

    plt.plot(n, data[0], 'o', label='obtained data')
    plt.plot(n, reg.intercept + reg.slope*n, 'r--', label='fitted line')
    plt.xlabel('Resonance nr. [n]')
    plt.ylabel('Frequency [Hz]')
    plt.title(data[1])
    plt.grid(color='black', linestyle = '--', linewidth = 0.25)
    plt.legend()
    plt.show()

print('\n')
