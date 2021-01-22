# Enter your code here. Read input from STDIN. Print output to STDOUT


def hundreds(n):
    if n==0:
        return 0
    h = {100:"One Hundred",200:"Two Hundred",300:"Three Hundred",400:"Four Hundred",500:"Five Hundred",600:"Six Hundred",
         700:"Seven Hundred",800:"Eight Hundred",900:"Nine Hundred"}
    twenties = {11:'Eleven',12:'Twelve',13:"Thirteen",14:'Fourteen',15:'Fifteen',
               16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',10:'Ten'}
    if n in h:
        return h[n]
    tens = {2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
    ones = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
    s = []
    x = str(n)
    if len(x)==1:
        return ones[n]
    if len(x)==2:
        if n>=10 and n<20:
            return twenties[n]
        if n/10 in tens:
            return tens[n/10]
        s.append(tens[int(x[0])])
        s.append(ones[int(x[1])])
        return ' '.join(s)
    s.append(ones[int(x[0])])
    s.append('Hundred')
    if n%100 <10:
        s.append(ones[n%100])
        return ' '.join(s)
    if n%100>=10 and n%100<20:
        s.append(twenties[n%100])
        return ' '.join(s)
    if int(x[2]) == 0:
        s.append(tens[int(x[1])])
        return ' '.join(s)
    s.append(tens[int(x[1])])
    s.append(ones[int(x[2])])
    return ' '.join(s)

def result(n):
    words = {1:'Thousand',2:'Million',3:'Billion'}
    s = []
    l=len(str(n))
    i = 1
    if l<=3:
        return hundreds(n)
    while i < l//3 +1:
        r = []
        if n%1000 !=0:
            r.append(hundreds(n%1000))
        n = n//1000
        if n%1000 !=0:
            r.append(words[i])
        if n<1000:
            r.append(hundreds(n))
            r.reverse()
            s.append(' '.join(r))
            break
        i+=1
        if len(r)!=0:
            r.reverse()
            s.append(' '.join(r))
    s.reverse()
    return ' '.join(s)

for _ in range(int(input())):
    n = int(input())
    if n!=0:
        print(result(n))
    else:
        print('Zero')
