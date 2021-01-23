# Enter your code here. Read input from STDIN. Print output to STDOUT
def switch(h) :
    return {
        0 : "Saturday",
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
    }[h]
 
def Zellercongruence(day, month, year) :
    if (month == 1) :
        month = 13
        year = year - 1
 
    if (month == 2) :
        month = 14
        year = year - 1
    q = day
    m = month
    k = year % 100;
    j = year // 100;
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    return switch (h)
    
for _ in range(int(input())):
    s = list(map(int,input().split(' ')))
    e = list(map(int,input().split(' ')))
    count = 0
    if s[0] == e[0]:
        if s[2] != 1:
            s[1]+=1
        for i in range(s[1],e[1]+1):
            if Zellercongruence(1,i,s[0]) == 'Sunday':
                count+=1
        print(count)
    else:
        if s[2] != 1:
            s[1]+=1
        for i in range(s[0],e[0]+1):
            if i == s[0]:
                for j in range(s[1],13):
                    if Zellercongruence(1,j,i) == 'Sunday':
                        count+=1
            elif i == e[0]:
                for j in range(1,e[1]+1):
                    if Zellercongruence(1,j,i) == 'Sunday':
                        count+=1
            else:
                for j in range(1,13):
                    if Zellercongruence(1,j,i) == 'Sunday':
                        count+=1
        print(count)
