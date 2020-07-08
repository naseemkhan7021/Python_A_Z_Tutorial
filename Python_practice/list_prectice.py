# list and list coprahesive prectice
#1 seple list
'''
x=['naseem','khan','hellow']
p=[]
for i in x:
    p.append(i[::-1])
print(p)
 '''   
# 2 list coprehesive
'''
p=[i[::-1] for i in x]
print(p)
'''

#1 seple list
'''
from math import factorial as fl
x=[1,3,3,4]
p=[]
for i in x:
    p.append(fl(i))
print(p)
'''
# 2 list coprehesive
'''
p=[fl(i) for i in x]
print(p)
'''

# 3 map() fungtion
'''
p=list(map(fl,x))
print(p)
'''

#1 seple list
'''
f=['123',234,'ansd',34.56,'kansdf',23+3j]
for i in f:
    if type(i)==str:
        print([i])
    '''    
# 2 list coprehesive in  if condition
'''
r=[i for i in f if type(i)==str]
print(r)
'''
#1 seple list
'''
f=[2,34,3,5,5,3.3,3.45]
en=[]
od=[]
for i in f:
    if i%2==0:
        en.append(i)
    else:
        od.append(i)
print('even no. ',en,'\n','odd no. ',od)
'''
# 2 list coprehesive in if else condition
'''
e_o=[str(i)+' is even' if i%2==0 else str(i)+' is odd' for i in f]
print(e_o)
'''

#1 seple list
'''
f=[2,34,3,5,-5,3.3,-3.45,0]
a=[]
for i in f:
    if i>0:
        a.append(str(i)+'+pst')
    elif i<0:
        a.append(str(i)+'-neg')
    else:
        a.append(str(i)+' zero')

print(a)
'''
# 2 list coprehesive in if else condition
'''
a=[str(i)+' +ve' if i>0 else str(i)+' -ve' if i<0 else str(i)+' zero'
    for i in f]
print(a)
'''
#1 seple list
'''
f=[]
for i in range(5):
    f.append([])
    for slist in range(5):
        f[i].append(slist)
print(f)
'''
# 2 list coprehesive nested loops
'''
f=[[slist for slist in range(5)] for i in range(5)]
print(f)
'''

#1 seple list
'''
x=['naseem','khan','hellow']
f=[]
for i in x:
    if len(i)>4:
        f.append(i)
print(f)
'''
# 2 list coprehesive in if condition
'''
f=[i for i in x if len(i)>4]
print(f)
'''
# inbuilt method of list
'''
s=['123',234,'ansd',34.56,'kansdf',23+3j]

# for deliting methods
s.pop() # remove last eliment
print(s)
s.remove('123') # remove specific eliment
print(s)
del s[2] # delite idexing eliment
print(s)
# for adding method
s.append('123') # add elimen in last
print(s)
s.insert(2,'naseem') # add specific location
print(s)
l=s.copy()  # for copy the list
print(l)
n=[1,2,2,3,45]
s.extend(n)   # for addin one list to extend another list
print(s)

'''
