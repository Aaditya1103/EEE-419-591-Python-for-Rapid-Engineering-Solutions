################################################
#     Name:- Aaditya Sakhardande               #
#     ASU ID:- 1233720594                      #
#     Email:- aadityasakhardande@gmail.com     #
#     Date:- 01/29/2025                        #
################################################

import numpy as np

def generate_prime_numbers(start, end):

    primes = [2] 
    # Loop through each number in the specified range to check if it's prime
    for number in range(start, end + 1):
        is_prime = True
        
        # Check divisibility
        for p in primes:
            if number % p == 0:  
                is_prime = False
                break
            if p > np.sqrt(number): 
                break
        
        # If the number is prime, append it to the list
        if is_prime:
            primes.append(number)
    # Return the list of prime numbers
    return primes

# Generate prime numbers between 3 and 10000
my_prime_list = generate_prime_numbers(3, 10000)
print(my_prime_list)
