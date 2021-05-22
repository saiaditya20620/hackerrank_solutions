def beautifulDays(i, j, k):
    l=[]
    b=0
    for n in range(i,j+1):
        temp=n
        rev = 0
        b=0
        while (n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10
        x=((abs(temp-rev)) % k)
        l.append(x)
    for j in l:
        if j==0:
            b+=1
    return b
