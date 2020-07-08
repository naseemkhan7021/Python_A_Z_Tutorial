# exe.1----------------find Area of triangla 
'''H = int(input('enter hieght of triangle  '))
B = int(input('enter base of triangle  '))
A = H*B//2
print('Area =',A)'''

# exe.2------------>converte Centigrade to Fahrenheit
'''C = int(input('centigrade tempreture = '))
F = (C * 9/5) + 32
print('the Fahrenheit=' , F)'''

# exe.3------------------->find velum of cone and sphere
'''H = int(input('enter height ='))
R = int(input('enter rediun ='))
p = 3.14
Cv = 1/3*p*(R**2)*H
Sv = 4/3*p*(R**3)
print('cone velum =',Cv, 'sphere velum =' , Sv)'''

# exe.4--------------->find total amount and copaund intrese
'''P = int(input('principal ='))
T = int(input('time ='))
R = int(input('rate of intress ='))
CI = P*(1+R/100)**T
Amt = P + CI
print('copaund intress =',CI, 'amount =',Amt)'''

#  exe.5---------------> this program is finding Factorial number in recarsion method

'''def f_t_num(n):
    if n == 1:
        return n
    else:
        return n*f_t_num(n-1)

num = int(input('enter your Factorial limit ='))
s_r = ('sorry boss')

if num < 0:
    print(s_r.center(len(s_r)+8,'!'))
elif num == 0:
    print('your float is= 1')
else:
    print('your number is=',num,'it factorial =',f_t_num(num))'''

# exe.5---------------> this program is finding Factorial number in looping method
# it's for loop
'''
num1 = int(input('entar your Factorial limite ='))
fac = 1
for i in range(1,num1+1):
    fac = i*fac
    print(i)
print('your factorial num =',num1,'and it\'s factorial is =',fac)
'''
# it's will loop
'''
num2 = int(input('entar your Factorial limite ='))
fac2=1
i=1
while i<=num2:
    fac2 =fac2 * i
    i = i + 1

print('your factorial num =',num2,'and it\'s factorial is =',fac2)'''

#  exe.5---------------> this program is finding Fibonethis seriase
'''
n1 = int(input('write your limet of fibonethis seriase = '))
def fibo_ser(n):
   
   a = 0
   b = 1
   if n ==1:
      return(a)
   elif n == 2:
      return(a,b)
   else:
      return(a,b,end=' ,')
      for i in range(n-2):
            c = a+b
            a = b
            b = c
            return(d,end=' ')
print(fibo_ser(n1))
# for i in range(1,11):
#    print(i,end=' ')
# print(fibo_ser(n1))--------->this is not work'''


# secund method
'''
a,b=0,1

print(a,end=' ')
for i in range(10+1):
   a,b=b,a+b
   print(a,end=' ')
'''
'''
fec=1
for i in range(1,5+1):
   fec*=i
print(fec)
'''

'''    recurse method of fectorial
def fect(n):
   if n==0:
      return 1
   else:
      return n*fect(n-1)

print(fect(6))
'''

''' interective method for fectorial
def fect(n):
   f=1
   if n==0:
      return 1
   else:
      for i in range(1,n+1):
         f*=i
      return f

print(fect(6))
'''

# finding leap year

'''year = int(input('entar year for chacking leap year ='))
y=year%4
x=year%100
z=year%400
if y==0 or x != 0 and z==0:
   print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))'''

# greatest of 4 number using if elif else mathot

'''w,x,y,z = input('enar 4 numbers to find greatest =').split()
a=int(w)
b=int(x)
c=int(y)
d=int(z)
if a>b and a>c and a>d:
   if a==b or a==c or a==d:
      print(a,' is many tyme')
   print('the greatest is =',a)
elif b>a and b>c and b>d:
   if b==a or b==c or b==d:
      print(b,' is many tyme')
   print('the greatest is =',b)
elif c>a and c>b and c>d:
   if c==a or c==b or c==d:
      print(c,' is many tyme')
   print('the greatest is =',c)
elif d>a and d>b and d>c:
   if d==a or d==b or d==c:
      print(d,' is many tyme')
   print('the greatest is =',d)
else :
   print('all are equale')'''

# greatest of 4 number using 'nested' if else method

'''w,x,y,z = input('enar 4 numbers to find greatest =').split()
a=int(w)
b=int(x)
c=int(y)
d=int(z)
if a>=b:
   if a>=c:
      if a>=d:
         print(a,' is greatest')
      else:
         print(d,' is greatest')
   else:
      if c>=d:
         print(c,' is greatest')
      else:
         print(d,' is greatest')
else:
   if b>=c:
      if b>=d:
         print(b,' is greatest')
      else:
         print(d,' is greatest')
   else:
      if c>=d:
         print(c,' is greatest')
      else:
         print(d,' is greatest')'''
   

# divide by 3 but not 7

'''u = int(input('entar number =  '))
if u%3==0 and u%7 != 0:
   print(u,' is divisible by 3 but not 7')
elif u%7==0:
   print(u,' is dicisible by 7')
else:
   print('pleas try another number')'''



# find student fail or pass if pass find parcentateg
   
'''n,a = input('entar your name and age ').split()
r = int(input('entar your roll number '))
h = int(input('etar Hindi mark = '))
e = int(input('entar Englisg mark = '))
m = int(input('entar Math mark = '))
t = h+e+m
print(t,' is your total mark')
p = t/300*100
s=0
if h<40:
   s+=1
if e<40:
   s+=1
if m<40:
   s+=1
if s==0:
   print(p,'is your parsentage')
   if p>80:
      print('A great')
   elif p<80 and p>=70:
      print('B great')
   else:
      print('C great')
   print('your are pass')
if s==1:
   print('your are re-exame')
   print(s,'is your sub fails')
elif s>=2:
   print('you are fail')
   print(s,'is your sub fails')'''

# find root (ax**2+bx+c=0) x = ?
'''import math
n1,n2,n3=input('entar num a , num b and num c = ').split()
a=int(n1)
b=int(n2)
c=int(n3)
d = (b**2)-(4*a*c)
print('Discriminat = ',d)
if d>0:
   x1 = ((-b)+math.sqrt(d))/(2*a)
   x2 = ((-b)-math.sqrt(d))/(2*a)
   print('it is real number and it root1 = ',x1,
         ' root2 = ',x2)
elif d==0:
   x1 = (-b)/(2*a)
   x2 = x1
   print('it is equal number and it root1 = ',x1,
         ' root2 = ',x2)

else:
   print('it is imaginary number')'''



#fibonecci series recuresn method
'''
n=int(input('entar number = '))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b,end=' ')
    i=0
    while i<(n-2):
        c=a+b
        a=b
        b=c
        print(b,end=' ')
        i+=1
    
'''


# find purson age finder
'''
import datetime
print('pleas folow the comment and entar what it ask')
y=int(input('entar Birth year = '))
m=int(input('entar Birth month = '))
d=int(input('entar Birth day = '))
dob = datetime.date(y, m, d)

def age(n):
    today = datetime.date.today()
    years = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        years -= 1
    return years

def age2(t):
    today = datetime.date.today()
    this_year_birthday = datetime.date(today.year, dob.month, dob.day)
    if this_year_birthday < today:
        years = today.year - dob.year
    else:
        years = today.year - dob.year - 1
    return years
print(f'your age is {age(dob)}')

'''

