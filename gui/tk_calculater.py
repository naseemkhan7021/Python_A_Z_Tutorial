from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.filedialog import *

def exit():
    wd.event_generate('<<Exit>>')

memory=""
def press(num):
    global memory
    memory+=str(num)
    x.set(memory)

def pressequal():
    try:
        global memory
        total = eval(memory)  #eval() inbuilt function which convert string type value to numeric value 
        y.set(total)          #eval() ==>automatic evalute means + then +   #   e2.insert(10,(e1.get()))
        toshow.set(f'{memory} = {total} ')
    except Exception:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write proper)")

def pressclear():
    global memory
    memory=''
    x.set(memory)
    y.set("0")

def pow1():
    try:
        global memory
        A=int(memory)*int(memory)
        y.set(A)
        toshow.set(f'Power of {memory} = {A}')
    except ValueError:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write only a Number)")

def pow2():
    try:
        global memory
        A=int(memory)*int(memory)*int(memory)
        y.set(A)
        toshow.set(f'Dubbel Power of {memory} = {A}')
    except ValueError:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write only a Number)")


def sqrt():
    try:
        from math import sqrt
        A=sqrt(int(memory))
        y.set(A)
        toshow.set(f'Square root of {memory} = {A}')
    except ValueError:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write only a Number)")

def factorial():
    try:
        global memory
        from math import factorial as f
        A=f(int(memory))
        y.set(A)
        toshow.set(f'factorial of {memory} = {A}')
    except ValueError:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write only a Number)")

def sin():
    try:
        global memory
        from math import sin as s
        A=s(int(memory))
        y.set(A)
        toshow.set(f'sin of {memory} = {A}')
    except ValueError:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write only a Number)")

def cos():
    try:
        global memory
        from math import cos as c
        A=c(int(memory))
        y.set(A)
        toshow.set(A)
        toshow.set(f'cos of {memory} = {A}')
    except ValueError:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write only a Number)")

def ten():
    try:
        global memory
        from math import tan as t
        A=t(int(memory))
        y.set(A)
        toshow.set(A)
        toshow.set(f'ten of {memory} = {A}')
    except ValueError:
        messagebox.showinfo("Error","sumthing is error !!! \n (Pleas write only a Number)")


def press_undo():
    global memory
    lis=list(memory)
    lis.pop()
    x.set(lis)




wd=Tk()
wd.title('New Calculater')
wd.geometry('333x550+0+0')

menubar=Menu(wd)

viewm=Menu(menubar,tearoff=0)

viewm.add_command(label="Standard")
viewm.add_command(label="Scientific")

viewm.add_separator()
viewm.add_command(label="Programmer")
viewm.add_command(label="Exit",command=exit)

menubar.add_cascade(label="View",menu=viewm)

# --end view menu-->

editm=Menu(menubar,tearoff=0)

editm.add_command(label="Copy")
editm.add_command(label="pest")

# ---stat submenu--->

historym=Menu(editm,tearoff=0)

historym.add_command(label="Copy history")
historym.add_command(label="Edit")

historym.add_separator()

historym.add_command(label="Cancel edit")
historym.add_command(label="Clear")

editm.add_cascade(label="History",menu=historym)
# --end historym sub menu-->

menubar.add_cascade(label="Edit",menu=editm)

# --end edit menu-->

helpm=Menu(menubar,tearoff=0)

helpm.add_command(label="View help")
helpm.add_separator()
helpm.add_command(label="About Calculator")

menubar.add_cascade(label="Help",menu=helpm)
# for output
y=StringVar()
e2=Entry(wd,textvariable=y,justify=RIGHT,width=30,font="Times 16 bold",bg='lightblue')                             # e1.place()  # this is for user definde palce
e2.grid(row=0,column=0,columnspan=5,pady=3)                    # e1.pack()  #this is for any place
y.set('Here is your answere')
# for input
x=StringVar()
e1=Entry(wd,textvariable=x,bg='lightblue',justify=RIGHT,width=30,font="Times 16 bold")
e1.grid(row=1,column=0,columnspan=5)
x.set('enter your expression')


#Buttons
# secund row
Allclearb=Button(wd,text="C",fg="black",bg="red",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=pressclear).grid(row=2,column=0)
PMb=Button(wd,text="+/-",fg="black",bg="lightgreen",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=lambda : press("-")).grid(row=2,column=1)
Lastclearb=Button(wd,text="<-",bg="lightgreen",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=press_undo).grid(row=2,column=2)
bdivid=Button(wd,text='/',fg="black",bg="lightgreen",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=lambda : press("/")).grid(row=2,column=3)
bsqrt=Button(wd,text="√",fg="black",bg="lightgreen",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=sqrt).grid(row=2,column=4)


numbers = "789456123"
i = 0
bttn = []
for j in range(3,6):
    for k in range(3):
        bttn.append(Button(wd,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        bttn[i]["bg"]= "orange"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda : press(i)
        i += 1
# 3rd row
# b1=Button(wd,text='7',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(7)).grid(row=3,column=0,pady=3)
# b2=Button(wd,text='8',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(8)).grid(row=3,column=1,pady=3)
# b3=Button(wd,text='9',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(9)).grid(row=3,column=2,pady=3)
b5=Button(wd,text='*',fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=lambda : press("*")).grid(row=3,column=3,pady=3)
b4=Button(wd,text='x^2',fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=pow1).grid(row=3,column=4,pady=3)


# 4th row
# b6=Button(wd,text='4',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(4)).grid(row=4,column=0,pady=3)
# b7=Button(wd,text='5',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(5)).grid(row=4,column=1,pady=3)
# b8=Button(wd,text='6',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(6)).grid(row=4,column=2,pady=3)
b14=Button(wd,text='-',fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=lambda : press("-")).grid(row=4,column=3,pady=3)
b4=Button(wd,text='x^3',fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=pow2).grid(row=4,column=4,pady=3)

#5th row
# b11=Button(wd,text='1',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(1)).grid(row=5,column=0,pady=3)
# b12=Button(wd,text='2',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(2)).grid(row=5,column=1,pady=3)
# b13=Button(wd,text='3',fg="black",bg="white",font=('Arial',10),height=2,width=3,command=lambda : press(3)).grid(row=5,column=2,pady=3)
bpluse=Button(wd,text='+',fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=lambda : press("+")).grid(row=5,column=3,pady=3)
bfac=Button(wd,text="X!",fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=factorial).grid(row=5,column=4,pady=3)

# 6th row
b0=Button(wd,text='0',fg="black",font=('Arial',10),bg="orange",height=2,width=15, pady = 10,command=lambda : press(0)).grid(row=6,column=0,columnspan=2)
bpoint=Button(wd,text='.',fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=lambda : press(".")).grid(row=6,column=2)
bparsentge=Button(wd,text='%',fg="black",bg="lightblue",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=lambda : press("%")).grid(row=6,column=3,pady=3)
bequal=Button(wd,text='=',fg="black",bg="green",font=('Arial',10),height =6,width=4,padx=9, pady = 10,command=pressequal).grid(row=6,column=4,rowspan=2,pady=1)


# 7th row
bsin=Button(wd,text='sin',fg="black",bg="yellow",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=sin).grid(row=7,column=0,pady=3)
bcos=Button(wd,text='cos',fg="black",bg="yellow",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=cos).grid(row=7,column=1,pady=3)
bten=Button(wd,text='ten',fg="black",bg="yellow",font=('Arial',10),height =2,width=4,padx=9, pady = 10,command=ten).grid(row=7,column=2,pady=3)

# 8th row history
toshow=IntVar()
l=Label(wd,textvariable=toshow,bg="white",font=('Arial',10),fg="black").place(x=5,y=500)



wd.config(menu=menubar)     # for create menu bar
wd.mainloop()