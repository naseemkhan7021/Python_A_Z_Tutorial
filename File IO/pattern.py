a= int(input('enter number  of row = '))
print("sidha ya ulta ")
t=int(input("type 0 or 1 = "))
n=bool(t)

if n==True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print('*',end='')
        print()
else:
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print('*',end='')
        print()