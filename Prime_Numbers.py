# author: Tyler Elenberger
# created: 9/12/2019

import math
def countPrimes(n):
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        count = i * 2
        while count < n:
            sieve[count] = False
            count += i
    primes = []
    for i in range (n):
        if sieve[i] == True:
            primes.append(i)
    print(primes)
    print("There are: ",len(primes),"numbers")
        
        
itera = countPrimes(100)
