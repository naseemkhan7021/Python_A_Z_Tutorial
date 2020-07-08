# create a menu and submenu
from tkinter import *

wd=Tk()
wd.title('Menu Create')
wd.geometry('700x600')
menubar=Menu(wd)            #menubar user defined object of menu control

#File Menu
filemenu=Menu(menubar,tearoff=0)        #tearoff=0 menas to remove --. line
filemenu.add_command(label="New")       # to add submenu in file menu
filemenu.add_command(label="Open") 
filemenu.add_separator()               # this is draw a line which seperate the submenu
# filemenu.add_command(label="Save") 
filemenu.add_command(label="Save as") 
filemenu.add_separator()               # this is draw a line which seperate the submenu
filemenu.add_command(label="Close") 
filemenu.add_command(label="Exit") 


menubar.add_cascade(label="File",menu=filemenu) #to add all filemenu inside the File open

#    Edit menu

editmenu=Menu(menubar,tearoff=0)        #tearoff=0 menas to remove --. line
editmenu.add_command(label="Undo")       # to add submenu in file menu
editmenu.add_command(label="Rendo") 
editmenu.add_separator()               # this is draw a line which seperate the submenu
editmenu.add_command(label="Cut") 
editmenu.add_command(label="Copy") 
editmenu.add_command(label="Paste")
editmenu.add_separator()               # this is draw a line which seperate the submenu
editmenu.add_command(label="Delete") 

menubar.add_cascade(label="Edit",menu=editmenu)   #to add all filemenu inside the File open

#  submenu of submenu

save_m=Menu(filemenu)
save_m.add_command(label="save as new")
save_m.add_command(label="save now")

menubar.add_cascade(label="save",menu=save_m)


wd.config(menu=menubar)
wd.mainloop()