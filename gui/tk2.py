from tkinter import *

root = Tk()
root.title(' two fram here')
root.geometry('700x600')
frame = Frame(root)
b1 = Button(frame,text='hello button')
b1.pack(side= LEFT)
b2 = Button(frame,text='hello your name')
b2.pack(side= LEFT)

frame.pack()

frame2 = Frame(root)

b3=Button(frame2,text='advanse option')
b3.pack(side= LEFT)
b4=Button(frame2,text='close')
b4.pack(side= LEFT)

frame2.pack(side= BOTTOM)


root.mainloop()