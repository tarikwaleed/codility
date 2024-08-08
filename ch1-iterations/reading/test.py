h=10
for i in range(h,0,-1):
    for j in range(h-i):
        print(' ',end=' ')
    for k in range(i*2-1):
        print("*",end=' ')
    print()


