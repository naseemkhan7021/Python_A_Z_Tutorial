from threading import Thread
def display(a,b):
    print("a = ", a)
    print("b = ", b)

def square(a):
    print("square :  " ,a*a)

t=Thread(target=display, args=(10,20))
t.start()  # start() inbuilt function of Thread class
t.join()  # join() inbuilt function of Thread class
t1=Thread(target=square, args=(5,))
t1.start()