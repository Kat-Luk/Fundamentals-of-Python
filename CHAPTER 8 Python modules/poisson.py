# Write a function called poisson( k, lam ) that takes an integer k and a float lam and returns the result of the following equation:
# Poisson 
# P( k; λ ) = ( λ^k * e^(−λ) ) / k!

import math
def poisson(k, lam):
        result = ((math.e**-lam)*(lam**k))/math.factorial(k)
        return result

