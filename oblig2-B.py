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
plt.ylabel("Antall")
plt.grid(color='black', linestyle = '--', linewidth = 0.25)
plt.show()


'''
def multiplis(N, s):
    return  factorial(N) / (factorial(N/2 + s) * factorial(N/2 - s))

s = np.linspace(-25, 25, 1000)
alt_multiplis = multiplis(N, 0) * np.e**(-2*s**2 / N)

#plt.subplot(2, 1, 2)
plt.plot(alt_multiplis)

plt.show()
'''