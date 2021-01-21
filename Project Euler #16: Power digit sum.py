def sum_digits(n):
    return sum([int(a) for a in str(n)])

for _ in range(int(input())):
    n = int(input())
    print(sum_digits(2**n))
