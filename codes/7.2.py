import numpy as np
import matplotlib.pyplot as plt

# Given values of r(i), p(i), and k(i)
r_values = [0.05029142-0.14322607j, 
            0.06019142+0.15662107j, 
            -0.06024359+0.02138604j, 
            -0.07019319-0.02318604j]

p_values = [0.87475217+0.0435749j, 
            0.82465217-0.0455749j, 
            0.94327798+0.1045852j, 
            0.93427798-0.10486352j]

k_values = [3.20e-5, 0, 0, 0]

# Time indices
n_values = np.arange(31)  # n values up to 30

# Compute h(n)
hn_values = np.zeros_like(n_values, dtype=np.complex128)
for n in n_values:
    for i in range(len(r_values)):
        hn_values[n] += r_values[i] * (p_values[i] ** n)
    for j in range(len(k_values)):
        if n - j >= 0:
            hn_values[n] += k_values[j]

# Plot
plt.stem(n_values, np.abs(hn_values))
plt.xlabel('$n$')
plt.ylabel('$|h(n)|$')
plt.title('Magnitude of $h(n)$')
plt.grid(True)
plt.show()
