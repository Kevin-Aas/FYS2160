from random import uniform
import matplotlib.pyplot as plt
import numpy as np

Ctb = 5
N = 80000
nstep = 15*N
tau = N
Tt = np.zeros(nstep, 1)
Tb = np.zeros(nstep, 1)
Tt[0] = 1
Tb[0] = -1
Tr = -1

for i in range(1, nstep):
    r = uniform(-2, 2)
    DT = Tt[i-1] - Tb[i-1]
    if r<DT:
        Tt[i] = Tt[i-1] - 1/N
        Tb[i] = Tb[i-1] + Ctb/N
    else:
        Tt[i] = Tt[i-1] + 1/N
        Tb[i] = Tb[i-1] - Ctb/N

