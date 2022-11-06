import numpy as np
import matplotlib.pyplot as plt

# Define quantities:
wb = 6 * 10**(-26)          # m^2
c = 0.1                     # *
rho = 0.05                  # kg/m^2
m = 1                       # kg
k = 1.380649 * 10**(-23)    # Boltzmann

beta = (1 + 2*c) / (1 - c)

# Find the equilibrium radius and maximum radius:
r_0 = np.sqrt(m / (4*np.pi*rho))
r_max = r_0*np.sqrt(2/beta + 1)

# Makes a list of radii from initial to maximum:
r = np.linspace(r_0, r_max, 1000)

# Makes list the eqvivalent strain for each radii:
epsilon = (r/r_0)**2 - 1

# Finds the surface tension at temperature T:
T = 300
sigma = k*T / (wb*(1-c)) * np.log((1+beta*epsilon) / (1-beta*epsilon/2))

# Plots
plt.axvline(x = epsilon[-1], color='tomato', linestyle="--", label=f"$\epsilon = ${epsilon[-1]:.2f}")
plt.plot(epsilon, sigma, color="dodgerblue")
plt.xlabel("$\epsilon$ [*]")
plt.ylabel("$\sigma$  [N/m]")
plt.title("Surface tension $\sigma$ over membrane strain $\epsilon$")
plt.grid(color='black', linestyle = '--', linewidth = 0.1)
plt.legend()
plt.show()