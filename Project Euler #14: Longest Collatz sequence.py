# Enter your code here. Read input from STDIN. Print output to STDOUT
result = [False] * 5000001
nmax=0
m = 0
def answer(n):
    global nmax,m
    count = 0
    curr = n
    if n == 0:
        result[n] = (m,count)
    else:
        while n!=1:
            if n <5000001 and result[n]:
                count+=result[n][1]
                break
            elif n%2 == 0:
                n=n//2
                count+=1
            else:
                n= (3*n + 1)//2
                count+=2
        if count>=nmax:
            m = curr
            nmax=count
        result[curr] = (m,count)
[answer(i) for i in range(5000001)]
for _ in range(int(input())):
    n = int(input())
    if n==0:
        print(0)
    else:
        print(result[n][0])
