from cmath import exp
from math import factorial
from random import randint, random
import numpy as np
import matplotlib.pyplot as plt
import random

N=50
s=np.zeros(10000)

for i in range(10000):
    random=np.random.choice([-1, 1], N)
    S_plus=0
    S_min=0

    for k in range(N):
        if random[k]==1:
            S_plus +=1
        else:
            S_min += 1
    s[i]= (S_plus - S_min)/2


plt.plot(s, '.')
plt.xlabel("M")
plt.ylabel(r"$E^*$", rotation=0)
plt.grid(color='black', linestyle = '--', linewidth = 0.25)
plt.show()

plt.hist(s, 25)
plt.xlabel(r"$E^*$")
plt.ylabel("Antall mikrotils.")
plt.grid(color='black', linestyle = '--', linewidth = 0.25)
plt.xlim([-15, 15])
plt.show()

plt.subplot(2, 1, 1)
plt.hist(s, 25)
plt.xlabel(r"$E^*$")
plt.ylabel("Antall mikrotilstander")
plt.grid(color='black', linestyle = '--', linewidth = 0.25)
plt.xlim([-15, 15])

s = np.linspace(-15, 15, 500)
alt_multiplis = 2**N * np.e**(-2*s**2 / N)

plt.subplot(2, 1, 2)
plt.plot(s, alt_multiplis)
plt.grid(color='black', linestyle = '--', linewidth = 0.25)
plt.xlabel("s")
plt.ylabel(r"$\Omega(50, s)$")
plt.xlim([-15, 15])
plt.show()

