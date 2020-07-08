from threading import Thread
def display(a,b):
    print("a = ", a)
    print("b = ", b)

for i in range(5):
    t=Thread(target=display, args=(10,20))
    t.start()  # start() inbuilt function of Thread class