t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = -1
    for a in range(3,n//3+1):
        b = (n**2 - 2*a*n)/(2*n - 2*a)
        c = n - b - a
        if b==int(b) and a*b*c > ans: ans = a*b*c
    print(int(ans))
