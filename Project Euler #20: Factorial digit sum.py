import math

def sum_numbers(n):
    result = math.factorial(n)
    return sum([int(char) for char in str(result)])

for _ in range(int(input())):
    n = int(input())
    print(sum_numbers(n))
