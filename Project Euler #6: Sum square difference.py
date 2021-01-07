def squaresum(n):
    """Return the sum of squares of natural numberes upto including n"""
    return (n*(n+1)*(2*n+1))//6
def naturalsquare(n):
    """Return the square of sum of all natural numbers upto n"""
    return ((n*(n+1))//2)**2

t = int(input().strip())  # total number of test cases
for a0 in range(t):
    n = int(input().strip())
    print(naturalsquare(n) - squaresum(n))
