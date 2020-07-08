import tkinter as tk
def selection():
    p1=p.get()
    j1=j.get()
    r1=r.get()
    # abhi baki hai 

    if p1==True and j1==True and r1==True:
        answer.config(text="all good you are exlent")
    else:

        ans="python : "+str(p1)+" Java : "+str(j1)+" Oracle : "+str(r1)  #str()  --> convert boolean value to string
        answer.config(text=ans)

wd=tk.Tk()
wd.title("CheckBox")
wd.geometry("400x300")

p=tk.BooleanVar()
j=tk.BooleanVar()
r=tk.BooleanVar()

c1=tk.Checkbutton(wd,text="python",var=p)
c2=tk.Checkbutton(wd,text="java",var=j)
c3=tk.Checkbutton(wd,text="Orecle",var=r)
c1.place(x=50,y=100)
c2.place(x=120,y=100)
c3.place(x=200,y=100)
b1=tk.Button(wd,text="ok",width=20,fg="green",bg="white",font=("Arial",13),command=selection)
b1.place(x=50,y=150)
answer=tk.Label(wd,fg="green",bg="white",font=("Arial",10))
answer.place(x=50,y=200)


wd.mainloop()
