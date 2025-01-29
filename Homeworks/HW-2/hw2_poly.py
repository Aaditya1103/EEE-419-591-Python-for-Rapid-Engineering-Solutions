################################################
#     Name:- Aaditya Sakhardande               #
#     ASU ID:- 1233720594                      #
#     Email:- aadityasakhardande@gmail.com     #
#     Date:- 01/29/2025                        #
################################################

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#Function to compute ax^2 + bx + c
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

#Define range and step size
step_size = 0.01
r_values = np.arange(0, 5 + step_size, step_size)

#Function to compute definite integral from 0 to r
def compute_integrals(a, b, c):
    return [quad(quadratic_function, 0, r, args=(a, b, c))[0] for r in r_values]

#Compute integrals for both sets of coefficients
integral_1 = compute_integrals(2, 3, 4)
integral_2 = compute_integrals(2, 1, 1)

#Plot results
plt.plot(r_values, integral_1, label="a=2, b=3, c=4", linewidth=2)
plt.plot(r_values, integral_2, label="a=2, b=1, c=1", linestyle="dashed", linewidth=2)

#Labels and title
plt.xlabel("Upper limit of integration (r)")
plt.ylabel("Computed Integral")
plt.title("Definite Integral of Quadratic Functions")
plt.legend()
plt.grid(True)

plt.show()
