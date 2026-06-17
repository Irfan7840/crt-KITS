n=int(input('Enter the value :'))
k=1
for i in range(1,n+1):
    k=1
    for j in range(1,n+1):
        print("{:1d}".format(k),end=" ")
        k+=2
    print()        