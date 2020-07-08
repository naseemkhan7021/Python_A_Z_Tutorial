'''
d1={'name':'naseem','age':34,'city':'mumbai'}
'''
'''
# same methodes and fungtion of dictionary
#pring key velue
for i in d:
    print(i)
for i in d.keys():
    print(i)
print()

for i in d:
    print(d[i])
for i in d.values():
    print(i)
print()

for i in d:
    print(i,':',d[i])
for i,p in d.items():
    print(i,':',p)
'''
'''
d['name']='samim' # uppdet velues
print(d)

d.pop('city')  # for remove key velue
print(d)
print()
d1=dict(d) # for copy dictionary
print(d1)
d2=d.copy()  # for copy dictionary
print (d2) 
'''


# nested dictionary
# you can also use nested list
'''
d2={'name':'samim','age':33,'city':'pune'}
d3={'name':'alim','age':37,'city':'Thana'}
d={1:d1,2:d2,3:d3}
print(d[1])
print(d[2]['age'])
print(d[3]['city'])
'''

# dictnary coprehansive
'''
d1={'name':'naseem','age':34,'city':'mumbai'}
a={i:v for i,v in d1.items()}
print(a)
'''
'''
a={i:'even' for i in range(1,21) if (i%2==0)}
print(a)
'''

'''
# nested if 
A={1:'one',4:'foure',6:'six',5:'five'}
d={k:v for k,v in A.items() if len(v)>=3 if k>3}
print(d)

# if else
name_age={'naseem':34,'samim':23,'alim':45,'salman':12,'6':19
          ,'rohit':83,'sharuk':89}
t={k:('young' if v<30 else 'old') for k,v in
   name_age.items()}
print(t)

#if elif else
t={k:('young' if v<=30 else 'old' if v<80 else 'sorry dai')
   for k,v in name_age.items()}
print(t)
'''
