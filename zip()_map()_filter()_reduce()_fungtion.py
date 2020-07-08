# zip() fugtion

# ziping two list
'''
a=['username','id','password']
b=['naseem','nk7021','na12%%$$']
profile=list(zip(a,b))
print(profile)
# output = [('username', 'naseem'),
# ('id', 'nk7021'), ('password', 'na12%%$$')]
'''

# ziping 4 list   --->list,tuple or set
'''
a=['name','roll num','mark','strinme']
b=['naseem',34,54,'IT']
c=['samim',45,67,'Science']
d=['salman',56,76,'commerce']
profile=list(zip(a,b,c,d)) #also make tubpe or set
print(profile)
'''
# unziping file
#any_veriable=zip(*ziped_file_name)
'''
any_veriable=zip(*profile)
print(list(any_veriable))
'''


# map() fungtion----(it is only normal problem not condition stetment)

# map use for creating new list

# using fungtion
'''
def add(a):
    return a*a
# for creating list
l=[int(i) for i in input('enter no to creat list = ').split(',')]
maped=list(map(add,l)) #also make tubpe or set
print(maped)
# output [4, 9, 16, 25, 9, 16]
'''

# using lambda fungtion
'''
l=[int(i) for i in input('enter no to creat list = ').split(',')]
l_meped=list(map(lambda a: a*a,l)) #also make tubpe or set
print(l_meped)
# output [4, 9, 16, 25, 9, 16]
'''
# operetion on two or more list
'''
# creating list whith using coprehesive
l_1=[int(i) for i in input('enter no to creat list 1 = ').split(',')]
l_2=[int(i) for i in input('enter no to creat list 2 = ').split(',')]
l_3=[int(i) for i in input('enter no to creat list 3 = ').split(',')]
l_meped=list(map(lambda a,b,c:a+b+c,l_1,l_2,l_3)) #also make tubpe or set
print(l_meped)
'''

# for macking nested list
'''
l=['naseem','khan','hellow']
l_meped=list(map(list,l))
print(l_meped)
'''



# filter() fungtion ----(same as map() but also use whitn condition stetment)

#filter is also use for creatin list (whith condition)
'''
def even(a):
    if a%2==0:
        return True
    else:
        return False

l=[int(i) for i in input('enter num = ').split(',')]
l_filter=list(filter(even,l))
print('even no.s = ',l_filter)
'''
# using lambda same program
'''
l=[int(i) for i in input('enter num = ').split(',')]
l_filter=list(filter(lambda a:a%2==0  ,l))
print('even no.s = ',l_filter)
'''


# reduse() fungtion 
'''
import functools as f   # for caling funtools module the reduce

l=[2,3,4,5,6,7]
a=f.reduce(lambda a,b: (a+b) ,l)
print(a)  # only run with bash camand


l=[int(i) for i in input('enter number = ').split(',')]  # for creating list coprehesive
a=f.reduce(lambda a,b: (a+b) ,l) 
print(a)  # only run with bash camand


l=[int(i) for i in input('enter number = ').split(',')]
a=f.reduce(lambda a,b: a*b,l)
print(a)    # only run with bash camand
'''

