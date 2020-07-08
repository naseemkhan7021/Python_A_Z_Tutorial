f=open("file.txt",'r')
print(f.tell())
print(f.readline())

f.seek(0)
# print(f.tell())
print(f.readline())
# print(f.tell())

f.close()