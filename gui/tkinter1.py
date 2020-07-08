from tkinter import *

root =Tk()


frame =Frame(root)
button1=Button(frame,text='start').pack(side=LEFT)
button2=Button(frame,text='search samthing you like').pack(side=RIGHT)
botton3=Button(frame,text='do samthinh').pack(side=LEFT)
frame.pack()

bottumframe=Frame(root)
button4=Button(bottumframe,text='what you to').pack(side=LEFT)
button5=Button(bottumframe,text='lest your thick').pack(side=LEFT)
button6=Button(bottumframe,text='close').pack(side=LEFT)
bottumframe.pack(side=LEFT)

lastframe=Frame(root)
button7=Button(lastframe,text='close').pack()
lastframe.pack(side=BOTTOM)


root.mainloop()