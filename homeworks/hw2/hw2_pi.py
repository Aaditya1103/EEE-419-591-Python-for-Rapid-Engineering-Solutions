##################################################

#          Name:- Aaditya Sakhardande            #
#          ASU ID:- 1233720594                   #
#          Email:- asakhar3@asu.edu              #
#          Date:- 01/29/2025                     #

##################################################
import numpy as np
from scipy.integrate import quad

#Function after applying substitution
def integrand(theta):
    return 2 

#Perform numerical integration of the function from 0 to pi/2
integral_value, error_estimate = quad(integrand, 0, np.pi / 2)

#Output the value of the integral.
print("Computed value of Pi: {:,.8f}".format(integral_value))

#Display the difference from numpy's value of pi to 15 decimal places
print("Difference from np.pi: {:,.15f}".format(np.pi - integral_value))