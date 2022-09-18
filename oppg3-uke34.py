import matplotlib.pyplot as plt

t = []
T_kald = []
T_varm = []

with open("metalblocks_lecture.tsv") as infile:
    for i in infile:
        t.append(float(i.split()[0]))
        T_kald.append(float(i.split()[1]))
        T_varm.append(float(i.split()[2]))
        
plt.plot(t, T_kald, label="T_kald")
plt.plot(t, T_varm, label="T_varm")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.25)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()

