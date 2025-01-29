##################################################
#          Name:- Aaditya Sakhardande            #
#          ASU ID:- 1233720594                   #
#          Email:- asakhar3@asu.edu              #
#          Date:- 01/29/2025                     #
##################################################

import cmath as cm 
import numpy as np  

def quadratic_solver(a, b, c):

    discriminant = b**2 - 4 * a * c
    denominator = 2 * a

    # Case 1: Discriminant > 0 (two roots)
    if discriminant > 0:
        sqrt_discriminant = np.sqrt(discriminant)  
        root1 = (-b + sqrt_discriminant) / denominator 
        root2 = (-b - sqrt_discriminant) / denominator 
        print(f"The equation has two real roots: x1 = {root1:.2f}, x2 = {root2:.2f}")

    # Case 2: Discriminant == 0 (one real double root)
    elif discriminant == 0:
        root = -b / denominator 
        print(f"The equation has a double root: x = {root:.2f}")

    # Case 3: Discriminant < 0 (two complex roots)
    else:
        sqrt_discriminant = cm.sqrt(discriminant) 
        root1 = (-b + sqrt_discriminant) / denominator 
        root2 = (-b - sqrt_discriminant) / denominator 
        print(f"The equation has two complex roots: x1 = {root1}, x2 = {root2}")
        
print("Solve the quadratic equation: ax^2 + bx + c = 0")
a = int(input("Enter the coefficient a (a ≠ 0): "))  
b = int(input("Enter the coefficient b: ")) 
c = int(input("Enter the coefficient c: "))  

if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    quadratic_solver(a, b, c)