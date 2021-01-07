import math

def is_prime(n):
    if n == 2:
        return True
    elif n%2 == 0: # even number can not be primes except 2
        return False
    else:
        for i in range(3,math.ceil(math.sqrt(n)) + 1,2):
            if n%i == 0:
                return False
        return True

prime = [i for i in range(3,104800,2) if is_prime(i)]
# creating a list of 10005 primes


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n == 1:
        print(2)
    else:
        print(prime[n-2])
