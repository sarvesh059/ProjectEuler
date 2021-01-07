def product(n,k):
    """ Taking a string n and an integer k as parameter
    Return Product of all the integers of n"""
    if n.count('0') >= 1: # if n contains zero then the product will be zero
        return 0
    else:
        r = 1
        for i in range(k):
            r *= int(n[i])
        return r

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = str(input())
    result = [product(num[i:i+k],k) for i in range(len(num)- k+1)]
    print(max(result))
