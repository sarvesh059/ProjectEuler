# DP approch
for _ in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    
    row = n-2
    while row >= 0:
        for i in range(len(s[row])):
            s[row][i] += max(s[row+1][i], s[row+1][i+1])
        row -= 1
    print(s[0][0])
    
# recursive approch
def func(arr,k=0,i=0):
    if k >=len(arr):
        return 0
    return arr[k][i] + max(func(arr,k+1,i+1),func(arr,k+1,i))
        

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split(' '))) for i in range(n)]
    print(func(arr))
