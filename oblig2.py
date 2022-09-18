from math import factorial
from tkinter.ttk import Style
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def micro_states(q, q_A, N_A, N_B):
    q_B = q - q_A    

    states_A = factorial(q_A + N_A - 1) / ( factorial(q_A) * factorial(N_A - 1) )
    states_B = factorial(q_B + N_B - 1) / ( factorial(q_B) * factorial(N_B - 1) )
    
    return states_A * states_B

for q_A in range(0, 7):
    s = micro_states(6, q_A, 2, 2)
    print(s)

###
states = []
q_A = np.linspace(0, 100, 101)
for q_Ai in q_A:
    s = micro_states(100, q_Ai, 50, 50)
    states.append(s)

states = np.array(states)
prob_states = states/sum(states)

plt.plot(q_A, prob_states)
plt.axvline(50, color='tomato', ls="--")
plt.xlabel(r"$q_A$")
plt.ylabel("Probability")
plt.grid(color='black', linestyle = '--', linewidth = 0.25)
plt.xticks(np.arange(101, step=10))
plt.yticks(np.arange(0.06, step=0.005))
plt.show()
