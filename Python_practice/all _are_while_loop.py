# prectice of whil loop in Itvedant class

# 1-exe --count the individual digit
'''
a=int(input('entar the number to count digits = '))
x=0
while a>0:
   a%10
   x+=1
   a//=10

print('the total digits are = ',x)
'''

# 2-exe --sume of individual digit
'''
a=int(input('entar the number to count digits = '))
s=0
while a>0:
   s+=(a%10)     # no varialble is use
   a//=10
print('the sum of idndividual digits are = ',s)
'''
# 3-exe --count and sume of idividual digits
'''
a=int(input('entar the number to count digits = '))
c=0
s=0
while a>0:
   s+=(a%10)
   c+=1
   a//=10

print('the digits are = ',c,' and sume of individual digits are = ',s)
'''

#find fectorial  increasing
'''n=int(input('entar number = '))
v=1
i=1
while i<=n:
    v*=i
    i+=1
print(v)
'''
#recurse method fectorial
'''
def ftol(n):
    v=1
    for i in range(1,n+1):
        v*=i
    return v
'''
'''
n=int(input('entar number = '))
print(ftol(n))
'''

# fide the fectorial of given number decreasing
'''
n=int(input('entar the number =' ))
s=1
while 1<=n:
    s*=n
    n-=1
print(s,' is fectorial')
'''

# find table
'''n=int(input('entar number = '))
i=1
while i<=10:
    t=n*i
    print(n,'*',i,'=',t)
    i+=1
'''

# fide the given number is armstrong or not like --input-->153--individual digits ka quebe than uska sum-output--->153
'''
a=int(input('entar the number to find armstorng or not = '))
x=a       #--Becouse when the while loop is Fulse than it is 0 isiliye 'a' ko alag veriable me asine kro
s=0
while a>0:
   s+=(a%10)**3  # no varialble is use
   a//=10
if s==x:
   print(x,' is armstrong number')
else:
   print(x,' is not armstrong number')
'''
   
# fide the given number is strong or not
'''
a=int(input('entar the number to find strong or not = '))
x=a 
s=0
while a>0:
   k=(a%10)  # no varialble is use
   s+=ftol(k)  # user defind fungtion
   a//=10
if s==x:
   print(x,' is strong number')
else:
   print(x,' is not strong number')
'''
# print *,**,***,****,*****....
'''
n=int(input('entar number to look * sape = '))
i=1
while i<=n:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    i+=1
    print()
'''

# print ******,*****,***,**,*...
'''
n=int(input('entar number to look * sape = '))
i=5
while i>=1:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    i-=1
    print()

#print ****,****,****,****,.....
'''
'''
n=int(input('entar number to look * sape = '))
i=1
while i<=n:
    j=1
    while j<=5:
        print('*',end='')
        j+=1
    i+=1
    print()
'''
# print 1,12,123,1234,12345.....
'''
n=int(input('entar number to look * sape = '))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    i+=1
    print()
'''

# print 1,22,333,4444,55555.....
'''
n=int(input('entar number to look * sape = '))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end='')
        j+=1
    i+=1
    print()
'''
# print 1 2 3 4,1 4 9 16......
'''
n=int(input('entar number to look * sape = '))
i=1
while i<=n:
    j=1
    while j<=5:
        print((j**i),end=',')
        j+=1
    i+=1
    print()
'''

#print 
#    *
#   **
#  ***
# ****
#*****
'''
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=i
    while k>=1:
        print('*',end='')
        k-=1
    i+=1
    print()
'''

#print
#    1
#   21
#  321
# 4321
#54321
'''
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=i
    while k>=1:
        print(k,end='')
        k-=1
    i+=1
    print()
'''

#print
#    1
#   12
#  123
# 1234
#12345
'''
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=1
    while k<=i:
        print(k,end='')
        k+=1
    i+=1
    print()
'''
#print
#    1
#   121
#  12321
# 1234321
#123454321
'''
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=1
    while k<=i:
        print(k,end='')
        k+=1
    p=i-1
    while p>=1:
        print(p,end='')
        p-=1
    i+=1
    print()
'''
#print
#     0
#    101
#   21012
#  3210123
# 432101234
#54321012345
'''
i=0
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=i
    while k>=0:
        print(k,end='')
        k-=1
    p=1
    while p<=i:
        print(p,end='')
        p+=1
    i+=1
    print()
'''
#print
#     0
#    010
#   01210
#  0123210
# 012343210
#01234543210
'''
i=0
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=0
    while k<=i:
        print(k,end='')
        k+=1
    p=i-1
    while p>=0:
        print(p,end='')
        p-=1
    i+=1
    print()
'''
#print
#     *
#    ***
#   *****
#  *******
# *********
#***********
'''
i=0
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=0
    while k<=i:
        print('*',end='')
        k+=1
    p=i-1
    while p>=0:
        print('*',end='')
        p-=1
    i+=1
    print()
'''

#print
# ******
# *    *
# *    *
# ******
'''
i=1
while i<=4:
    j=1
    while j<=6:
        if i==1 or i==4 or j==1 or j==6:
            print('*',end='')
        else:
            print(' ',end='')
        j+=1
    i+=1
    print()
'''
#print
#     0
#    010
#   01210
#  0123210
# 012343210
#01234543210
#01234543210
# 012343210
#  0123210
#   01210
#    010
#     0
#     1
#    121
#   12321
#  1234321
# 123454321
#12345654321
#12345654321
# 123454321
#  1234321
#   12321
#    121
#     1
'''
i=0
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    k=0
    while k<=i:
        print(k,end='')
        k+=1
    p=i-1
    while p>=0:
        print(p,end='')
        p-=1
    i+=1
    print()
x=0
while x<=5:
    y=1
    while y<=0+x:
        print(' ',end='')
        y+=1
    z=0
    while z<=5-x:
        print(z,end='')
        z+=1
    l=4-x
    while l>=0:
        print(l,end='')
        l-=1
    x+=1
    print()

i=1
while i<=6:
    j=1
    while j<=6-i:
        print(' ',end='')
        j+=1
    k=1
    while k<=i:
        print(k,end='')
        k+=1
    p=i-1
    while p>=1:
        print(p,end='')
        p-=1
    i+=1
    print()
t=1
while t<=6:
    j=1
    while j<=t-1:
        print(' ',end='')
        j+=1
    w=1
    while w<=7-t:
        print(w,end='')
        w+=1
    q=6-t
    while q>=1:
        print(q,end='')
        q-=1
    t+=1
    print()
'''




#print
#          0
#         101
#        21012
#       3210123
#      432101234
'''
i=0
while i<5:
    j=1
    while j<=10-i:
        print(' ',end='')
        j+=1
    k=i
    while k>=0:
        print(k,end='')
        k-=1
    p=1
    while p<=i:
        print(p,end='')
        p+=1
    print()
    i+=1
'''

#print
#1
#2 6
#3 7 10
#4 8 11 13
#5 9 12 14 15
'''
i=1
while i<=5:
    j=i
    p=1
    z=4
    while p<=i:
        print(j,end=' ')
        j+=z
        z-=1
        p+=1
    i+=1
    print()
'''

#print
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
'''
i=1  
z=1
while z<=5:            #z=1, #z=2   #,z=3     #z=4          #z=5
    j=i                #j=1, #j=2,  #,j=4     #j=7          #j=11
    p=1                 #1      ,1
    while p<=z:         #1<=1 #1<=2, #1<=3    #1<=4,        #1<=5
        print(j,end=' ') #print 1..2,3...4,5,6...7,8,9,10..11,12,13,14,15
        j+=1              #increasing velue
        p+=1
    print()
    print()
    i+=z   #increasing velue   #i=2,  #i=4   #i=7  #i=11
    z+=1   #increasing velue   #z=2,  #z=3   #z=4  #z=5
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
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(' ',end='')
        k+=1
    j=1
    while j<=i:
        if i==n or j==1 or j==i:
            print(a,end='')
        else:
            print(' ',end='')
        j+=1
    i+=1
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
i=1
while i<=n:
    j=1
    while j<=i:
        if i==n or j==1 or j==i:
            print(a,end='')
        else:
            print(' ',end='')
        j+=1
    i+=1
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
i=1
while i<=n:
    j=1
    while j<=(n+40)-i:
        print(' ',end='')
        j+=1
    k=1
    while k<=i:
        if k==1:
            print('*',end='')
        else:
            print(' ',end='')
        k+=1
    l=i-1
    while l>=1:
        if l==1:
            print('*',end='')
        else:
            print(' ',end='')
        l-=1
    print()
    i+=1

z=1
while z<=n:
    j=1
    while j<=z+39:
        print(' ',end='')
        j+=1
    k=n
    while k>=z:
        if k==n:
            print('*',end='')
        else:
            print(' ',end='')
        k-=1
    x=n-1
    while x>=z:
        if x==z:
            print('*',end='')
        else:
            print(' ',end='')
        x-=1
    print()
    z+=1
  '''      
    
