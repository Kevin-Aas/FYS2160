import matplotlib.pyplot as plt
import numpy as np
 
t = []
T1 = []
T2 = []

with (open("termokopper.txt") as infile):
    for i in infile:
        t.append(float(i.split()[0]))
        T1.append(float(i.split()[1]))
        T2.append(float(i.split()[2]))
        
plt.plot(t, T1, label="T1")
plt.plot(t, T2, label="T2")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.25)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()

tau = - 5000 / (np.log((44-22)/80-22))
print(tau)