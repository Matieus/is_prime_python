"""A simple algorithm that checks if a number is prime 
by dividing by successive numbers to the root of the checked number

This code uses the prime numbers property to make 
sequential numbers 6k, 6k+1, 6k+2, 6k+5, 6k+4, 6k+5 
for each k of the set of natural numbers from 0 to infinity
causes all primes greater than 5 to stack only on 6k+1 and 6k+5

example:
0
k = 0
6 * 0 + 1 = 1
6 * 0 + 2 = 2
6 * 0 + 3 = 3
6 * 0 + 4 = 4
6 * 0 + 5 = 5

k = 1
6 * 1 + 1 = 7
6 * 1 + 5 = 11

k = 2
6 * 2 + 1 = 13
6 * 2 + 5 = 17 

...
"""

"""
It happens because
6 * k + 1  =  2 * 3 * k + 1  =  2*(3*k + 1) - 1     it will always be odd
6 * k + 2  =  2 * 3 * k + 2  =  2*(3*k + 1)         will always be even (divisible by 2)
6 * k + 3  =  2 * 3 * k + 3  =  3*(2*k + 1)         will always be divisible by 3
6 * k + 4  =  2 * 3 * k + 4  =  2*(2*k + 2)         will always be even (divisible by 2)
6 * k + 5  =  2 * 3 * k + 5  =  2*(2*k + 2) + 1     it will always be odd

so all primes except 2 and 3 will be on 6k + 1 and 6k + 5
"""


rest = [1, 5]

def is_prime(prime: int) -> bool:
    if prime <= 1:
        return False 
    if prime%6 in rest or prime in [2, 3, 5]:
        n = ((prime + 1)**0.5)//1
        for p in range(2, int(n+1)):
            if p%6 in rest or p in [2, 3, 5]:
                if prime%p == 0:
                    return False     
        return True

    else:
        return False
