import tkinter as tk
from tkinter import messagebox
# def show():   # show() user defined function
#     messagebox.showinfo("message","sumthing is error !")

def sum1():
    a=int(t_a.get())
    b=int(t_b.get())
    c=a+b
    messagebox.showinfo("sum",f"sum of 2 numbers   = {c}")
def subract():
    a=int(t_a.get())
    b=int(t_b.get())
    c=a-b
    messagebox.showinfo("subract",f"subract of 2 numbers   = {c}")
def multiply():
    a=int(t_a.get())
    b=int(t_b.get())
    c=a*b
    messagebox.showinfo("multiply",f"multiply of 2 numbers   = {c}")
def devide():
    a=int(t_a.get())
    b=int(t_b.get())
    c=a/b
    messagebox.showinfo("devide",f"devide of 2 numbers  = {c}")

# main program
wd=tk.Tk()
wd.title('Employee Payroll')  #title() inbuilt function of Tk class, ro define title of window
wd.geometry('700x600')  #geometry() inbuilt function f Tk, there are pass two parameters width-->700 and height -->600
                        #x==> represent multiply
                        #geometry()==> to change the size of by defaul size of window
l_a=tk.Label(wd,text="enter first number :",fg="black",bg="white",font=("Arial",10))
l_a.place(x=10,y=50)
t_a=tk.Entry(wd,fg='white',bg='black',font=("Arial",10))
t_a.place(x=140,y=50)
l_b=tk.Label(wd,text="enter secund number :",fg="black",bg="white",font=("Arial",10))
l_b.place(x=10,y=80)
t_b=tk.Entry(wd,fg='white',bg='black',font=("Arial",10))
t_b.place(x=140,y=80)
# b1=tk.Button(wd,text="error messege",command=show ,fg='green',bg='white')#.pack()
#b1.pack()       #pack() inbuilt function of Button   #not use for change place
# b1.place(x=100,y=150)   # place() inbuilt function use for changing place
b2=tk.Button(wd,text="+",command=sum1,fg='green',bg='white')
b2.place(x=140,y=150)
b3=tk.Button(wd,text="-",command=subract,fg='green',bg='white')
b3.place(x=180,y=150)
b4=tk.Button(wd,text="x",command=multiply,fg='green',bg='white')
b4.place(x=210,y=150)
b5=tk.Button(wd,text="/",command=devide,fg='green',bg='white')
b5.place(x=250,y=150)

wd.mainloop()  #mainloop() inbuilt function ==> to hold output screen , mainloop() inbuilt method of TK

