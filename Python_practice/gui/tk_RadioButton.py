import tkinter as tk
def sel():
    g="Gender : "+gender.get()   # input to variable
    ans.config(text=g) #config()  = output=> inbuilt metho of label

wd=tk.Tk()

wd.title("Radiobutton")
wd.geometry("300x300")
gender=tk.StringVar()
R1=tk.Radiobutton(wd,text="male",value="Male",variable=gender,command=sel)
R2=tk.Radiobutton(wd,text="female",value="Fimale",variable=gender,command=sel)
R1.place(x=50,y=100)
R2.place(x=130,y=100)
ans=tk.Label(wd,fg="green",font=("Arial",18))
ans.place(x=50,y=150)
wd.mainloop()
