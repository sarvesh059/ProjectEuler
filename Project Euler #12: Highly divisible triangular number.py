n = int(input())

dividers = {1 : 3}
answers = {2: 2, 3 : 2}  # containes number of multiples of a number

def calcMinDividers():

    s = 3
    curMaxDiv = 2
    curDiv = 1
    while(curDiv <  1000):

        s += 1
        temps = s
        curDiv = 1  # Total number of divisors of a number
        # This below loop use the mathematics technique if n = a^x * b^y * c^z .....
        # Then the total number of divisors will be (x+1)*(y+1)*(z+1)*.....
        for i in range (2, int(s ** 0.5) + 1):
            countDiv = 0
            while temps % i == 0:
                countDiv += 1
                temps //= i
            curDiv *= countDiv + 1

        if temps != 1:
            curDiv *= 2

        answers[s] = curDiv
        # divisors of d(N(N+1)/2)= d(N/2)*d(N+1) if N is even else d((N+1)/2)*d(N)
        # Here s = N + 1
        if s % 2 == 0:
            curDiv = answers[s // 2]  * answers[s - 1]
        else:
            curDiv = answers[(s - 1) // 2]  * curDiv

        if curDiv > curMaxDiv :
            for i in range ( curMaxDiv, curDiv):
                dividers[i] = (s * (s - 1)) // 2
            curMaxDiv = curDiv

calcMinDividers()

for i in range(n):
    print(dividers[int(input())])
