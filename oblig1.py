import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
 
t = []
T1 = []
T2 = []

with open("termokopper.txt") as infile:
    for i in infile:
        t.append(float(i.split()[0]))
        T1.append(float(i.split()[1]))
        T2.append(float(i.split()[2]))
        
nStart = 34*2   # Punkt hvor begge temperaturene er på topp

t = np.array(t[nStart:])    # Tid fra topp temperatur
T_B = np.array(T1[nStart:]) # Bodum temperaturene fra topp temperatur
T_T = np.array(T2[nStart:]) # Temperfect temperaturene fra topp temperatur

slope, intercept, r_value, p_value, std_err = stats.linregress(t,np.log(T_B-22))
tau_B = -1/slope
print(f"Bodum tau = {tau_B:.2f}")

slope, intercept, r_value, p_value, std_err = stats.linregress(t,np.log(T_T-22))
tau_T = -1/slope
print(f"Temperfect tau = {tau_T:.2f}")

T_w = np.e**(-t/tau_B) * (88.5-22) + 22
plt.plot(t, T_w, "r--", label="Modell")
T_w_luft = -t*0.01/(1.256) + 88.5
plt.plot(t, T_w_luft)


T_w = np.e**(-t/tau_T) * (79.1-22) + 22
#plt.plot(t, T_w)

print(np.mean(T2[600:1000]))

plt.plot(t, T_B, label="Bodum")
#plt.plot(t[:6000], T_T[:6000], "tab:orange", label="Temperfect")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.25)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()
