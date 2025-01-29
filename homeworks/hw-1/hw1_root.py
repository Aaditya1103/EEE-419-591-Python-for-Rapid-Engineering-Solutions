################################################
#        Name:- Aaditya Sakhardande            #
#        ASU ID:- 1233720594                   #
#        Email:- aadityasakhardande@gmail.com  #
#        Date:- 01/29/2025                     #
################################################

import numpy as np

def my_sqrt(number, guess, tolerance):
    if np.abs(guess**2 - number) <= tolerance:
        return guess  
    else:
        new_guess = (guess + number / guess) / 2
        return my_sqrt(number, new_guess, tolerance)

TOLERANCE = 0.01

num = int(input("Enter the number to find the square root of: "))
initial_guess = int(input("Enter your initial guess: "))

result = my_sqrt(num, initial_guess, TOLERANCE)
print(f"The approximate square root of {num} is {round(result, 2)}.")
