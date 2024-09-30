import numpy as np
import matplotlib.pyplot as plt
import math

def logistic_map(r, x, n):
    trajectory = [x]
    for _ in range(n):
        x = r * x*(1-x)
        trajectory.append(x)
    return trajectory

# Parameters
r_values = np.linspace(2.8, 4.0, 50000)  # Range of parameter values for r
x0 = 0.2  # Initial condition
n = 99  # Number of iterations

# Generate bifurcation diagram
equilibrium_values = []
equilibrium_values_2 = []
equilibrium_values_3 = []
equilibrium_values_4 = []
equilibrium_values_5 = []
equilibrium_values_6 = []
equilibrium_values_7 = []
equilibrium_values_8 = []
for r in r_values:
    trajectory = logistic_map(r, x0, n)
    equilibrium_values.append(trajectory[-1])
    trajectory2 = logistic_map(r, x0, 100)
    equilibrium_values_2.append(trajectory2[-1])
    trajectory3 = logistic_map(r, x0, 101)
    equilibrium_values_3.append(trajectory3[-1])
    trajectory4 = logistic_map(r, x0, 102)
    equilibrium_values_4.append(trajectory4[-1])
    trajectory5 = logistic_map(r, x0, 103)
    equilibrium_values_5.append(trajectory5[-1])
    trajectory6 = logistic_map(r, x0, 104)
    equilibrium_values_6.append(trajectory6[-1])
    trajectory7 = logistic_map(r, x0, 105)
    equilibrium_values_7.append(trajectory7[-1])
    trajectory8 = logistic_map(r, x0, 106)
    equilibrium_values_8.append(trajectory8[-1])

# Plot bifurcation diagram
plt.plot(r_values, equilibrium_values, ',k', alpha=0.5)
plt.plot(r_values, equilibrium_values_2, ',k', alpha=0.5)
plt.plot(r_values, equilibrium_values_3, ',k', alpha=0.5)
plt.plot(r_values, equilibrium_values_4, ',k', alpha=0.5)
plt.plot(r_values, equilibrium_values_5, ',k', alpha=0.5)
plt.plot(r_values, equilibrium_values_6, ',k', alpha=0.5)
plt.plot(r_values, equilibrium_values_7, ',k', alpha=0.5)
plt.plot(r_values, equilibrium_values_8, ',k', alpha=0.5)
plt.xlabel('r')
plt.ylabel('Equilibrium Values')
plt.title('Bifurcation Diagram (Logistic Map)')
plt.show()


