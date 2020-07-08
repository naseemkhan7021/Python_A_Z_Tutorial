import numpy as np

#single dimensional array create
#array() inbuilt function of numpy library [] ==> array([])

a=np.array([3,4,5,8])

# here a is a user defined array object

print(a)

print(type(a))      # to display type of array object then use typ() nd means no. of dimensional

print(a.ndim)        #to ahso no. of dimension of array object a

print(a.dtype)          #to display datatype

a.dtype
#shope inbuilt method of numpy  to show the no. of rows and clumns in array object
a.shape			# here 4 is a no. of coulmns and row is 1(4,) (row,coulmns), means tuple means more than one element(  ,)
a.size		# to display the size of each element in bytes
a.nbytes		#to display no. of bytes occupied of array object nbyte=size of each element no. of elements
b=np.array([3,4,5,6,6])		# to store each element of array object b in float type
print(b)
print(b.dtype)
print(b.size)
