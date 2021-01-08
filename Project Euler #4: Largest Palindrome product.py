l = 101101
h = 1000000
def palindrome(n):
    s = str(n)
    return s == s[::-1]

result = [i*j for i in range(100,1000) for j in range(100,1000) if i*j >= l if i*j <= h if palindrome(i*j)]
result.sort()
for _ in range(int(input())):
    n = int(input())
    a=len(result) - 1
    while result[a] >= n:
        a-=1
    print(result[a])
 
