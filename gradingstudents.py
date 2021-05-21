k=[]
for i in l:
    if i<=35:
        k.append(i)
    if i>35:
        x=i%5
        if x>=3:
            i=i+abs(x-5)
            k.append(i)
        else:
            k.append(i)
return k
