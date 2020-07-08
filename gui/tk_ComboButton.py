# drope downe buttone

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk         # ttk inbult class which difine in tkinter library file and combobox define in ttk class

def show():
    m=month.get()
    messagebox.showinfo("Month select : ",m)

wd= tk.Tk()
wd.title("drowpe downe menu")
wd.geometry("500x400")
# combobox creat (drope downe meny)

month=ttk.Combobox(wd)      # month user define object of combox(dropedowne menu)

month["values"]=('HSC','SSC','Greguate','Post greguate')
month.place(x=100,y=50)
month.current(1)
b1=tk.Button(wd,text="ok",width=20,fg="green",bg="white",font=("Arial",13),command=show)
b1.place(x=70,y=150)

wd.mainloop()