import math

def is_prime(n):
    """Return True if a number is a prime number else False"""
    if n==1 or n==2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,n//2,2):
            if n%i == 0:
                return False
        return True
    
def perfectsquare(n):
    """Return True if a number is a perfect square"""
    sr = math.sqrt(n)
    return (math.floor(sr) - sr) == 0

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = 1
    for i in range(1,n+1):
        if res%i == 0:  # check product is already divisible by i
            pass
        elif is_prime(i): # we have to multiply all the prime numbers upto n
            res*=i
        elif perfectsquare(i) and i%2 != 0:  # for case of squares of prime numbers
            res*=int(math.sqrt(i))
        else:
            if i%2==0:  # case like 2,4,8,16,32 etc
                res*=2
            else: # cases like 3,9,27,81 etc
                res*=3
    print(res)
    # This solution is only valid upto n = 80 when n will be 81 according to above program it will multiply res by 9 but we have to multiply it by 3, Thus, giving wrong answer
