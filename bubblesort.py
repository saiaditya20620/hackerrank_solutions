swaps=0
for j in range(0,n-1):
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swaps += 1
print('Array is sorted in ',swaps,'swaps')
print('First Element:',a[0])
print('Last Element:',a[-1])
