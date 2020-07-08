#print
#*
#**
#***
#****
#*****
'''
for i in range(1,5+1):
    print('*'*i)
#    for j in range(1,i+1):
#        print('*',end='')
#    print()
'''

#print
#*****
#****
#***
#**
#*
'''
for i in range(5,0,-1):
    print('*'*i)
#    for j in range(1,i+1):
#        print('*',end='')
#    print()

'''
#print
#1
#12
#123
'''
for i in range(1,5+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
'''

#print
#12345
#1234
#123
#12
#1
'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()
'''
#print
#4444
#333
#22
#1
'''
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(i,end='')
    print()
'''

#print 
#    *
#   **
#  ***
# ****
#*****

for i in range(1,5+1):
    for j in range(1,6-i):
        print(' ',end='')
    print('*'*i)
    #for k in range(i,0,-1):
      #  print('*',end='')
    #print()


#print
#    1
#   21
#  321
# 4321
#54321
'''
for i in range(1,5+1):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(k,end='')
    print()
'''

#print
#    1
#   12
#  123
# 1234
#12345
'''
for i in range(1,5+1):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,i+1):
        print(k,end='')
    print()
'''

#print
#    1
#   121
#  12321
# 1234321
#123454321
'''
for i in range(1,5+1):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,i+1):
        print(k,end='')
    for p in range(i-1,0,-1):
        print(p,end='')
    print()
'''

#print

#     0
#    010
#   01210
#  0123210
# 012343210
#01234543210
# first method
'''
for i in range(0,5+1):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(0,i):
        print(k,end='')
    for p in range(i,-1,-1):
        print(p,end='')
    print()
 '''   
#print
#     0
#    101
#   21012
#  3210123
# 432101234
#54321012345
#first method
'''
for i in range(0,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(k,end='')
    for p in range(0,i+1):
        print(p,end='')
    print()
'''
'''
#secund method
for i in range(0,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(i,-1,-1):
        print(k,end='')
    for p in range(1,i+1):
        print(p,end='')
    print()
'''

#     54321
#    54320
#   54301
#  54012
# 50123
#01234
'''
for i in range(0,5):
    for j in range(1,5-i):
        print(' ',end='')
    for k in range(5,i,-1):
        print('*',end='')
    for p in range(0,i):
        print('*',end='')
    print()

i=1
while i<=5:
    p=2
    while p<=i:
        print(' ',end='')
        p+=1
    j=1
    while j<=5:
        if j==2 and j==3:
            continue
        print('*',end='')
        j+=1
    i+=1
    print()

'''
#print
#     *

#    **

#  ***

#****
'''
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end='')
    for k in range(1,i+1):
        print('*',end='')
    print()
    print()
'''

#print
#*****

#*   *

#*   *

#*   *

#*****
'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    print()
'''

#print
# ****
# *  *
# *  *
# ****
'''
for i in range(1,4+1):
    for j in range(1,4+1):
        if i==1 or i==4 or j==1 or j==4:
            print('*',end='')
            continue
        print(' ',end='')
    print()
'''
#print
#*
#**
#* *
#*  *
#*   *
#*    *
#*     *
#********
'''
n=int(input('entar number of row = '))
a=input('entar your sape that you like = ')
for i in range(n+1):
    for j in range(1,i+1):
        if  i==n or j==1 or j==i:
            print(a,end='')
            continue
        print(' ',end='')
    print()
'''
#print
#     *
#    **
#   * *
#  *  *
# *   *
#******
'''
n=int(input('entar number of row = '))
a=input('entar your sape that you like = ')
for i in range(n+1):
    for k in range(1,(n+1)-i):
        print(' ',end='')
    for j in range(1,i+1):
        if  i==n or j==1 or j==i:
            print(a,end='')
            continue
        print(' ',end='')
    print()
'''
#print
#        *
#       * *
#      *   *
#     *     *
#    *       *
#   *         *
#  *           *
# *             *
#*****************
'''
n=int(input('entar number of row = '))
a=input('entar your sape that you like = ')
for i in range(n+1):
    for j in range(1,(n+1)-i):
        print(' ',end='')
    for k in range(1,i+1):
        if k==1 or i==n:
            print(a,end='')
            continue
        print(' ',end='')
    for p in range(2,i+1):
        if p==i or i==n:
            print(a,end='')
            continue
        print(' ',end='')      
    print()
'''
# print
#       *
#      * *
#     *   *
#    *     *
#   *       *
#  *         *
# *           *
#*             *
# *           *
#  *         *
#   *       *
#    *     *
#     *   *
#      * *
#       *
'''       
n=int(input('entar number of row = '))
a=input('entar your sape that you like = ')

for z in range(1,n+1):
    for j in range(1,(n+1)-z):
        print(' ',end='')
    for k in range(1,z+1):
        if k==1:
            print(a,end='')
            continue
        print(' ',end='')
    for p in range(2,z+1):
        if p==z:
            print(a,end='')
            continue
        print(' ',end='')
    print()


for i in range(1,n+1):
    for j in range(1,i+1):
        print(' ',end='')
    for q in range(1,(n+1)-i):
        if q==1:
            print(a,end='')
            continue
        print(' ',end='')
    for t in range((n-1)-i,0,-1):
        if t==1:
            print(a,end='')
            continue
        print(' ',end='')
    print()
'''



