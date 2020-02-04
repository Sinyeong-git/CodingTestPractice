lis = {1,2,3,4,5,6,7,8,9,10}

for i in lis:
    if i % 2 == 0 : lis.remove(i)

for i in range(len(lis)):
    if lis[i] % 2 == 0 : del lis[i]

    