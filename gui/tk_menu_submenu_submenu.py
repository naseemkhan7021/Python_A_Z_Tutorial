from tkinter import *

root=Tk()
root.title('Menubar')
root.geometry("500x400")

menubar=Menu(root)          #for creating menu it's importent

# file menu
# ------------file menu start------------------------

filemenu=Menu(menubar,tearoff=0)        #tearoff=0 menas to remove --. line

filemenu.add_command(label="New file")
filemenu.add_command(label="New window")
filemenu.add_separator()
filemenu.add_command(label="Open file")
filemenu.add_command(label="Open folder")
filemenu.add_command(label="Open workspace")

#sub
# start sub-----
Reset_m=Menu(filemenu,tearoff=0)
Reset_m.add_command(label="All reset")
Reset_m.add_command(label="one reset")

# sub of sub
# start of sub of sub-----
Sum_rm=Menu(Reset_m,tearoff=0)

Sum_rm.add_command(label=" 1 ")
Sum_rm.add_command(label=" 2 ")
Sum_rm.add_command(label=" 3 ")
Sum_rm.add_command(label="more...")

Reset_m.add_cascade(label="sum reset",menu=Sum_rm)
# end sub of sub------

filemenu.add_cascade(label="Open Reset",menu=Reset_m)
# end sub---------

menubar.add_cascade(label="File",menu=filemenu)

# ----------file menu end----------------------


#edit menu       
# -------edit menu start---------

# main menu
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)

# --->
#submenu of 
Undo_m=Menu(editmenu,tearoff=0)

Undo_m.add_command(label="1 step")
Undo_m.add_command(label="2 step")

# sub of sub
last_m=Menu(Undo_m,tearoff=0)       # tearoff is use for removing deses in menu
last_m.add_command(label="Yes")
last_m.add_command(label="no")

Undo_m.add_cascade(label="all step",menu=last_m)

editmenu.add_cascade(label="Undo",menu=Undo_m)
# ---->

#submenu of  
Rendo_M=Menu(editmenu,tearoff=0)
Rendo_M.add_command(label="1 step")
Rendo_M.add_command(label="2 step")

# sub of sub
last_m=Menu(Rendo_M,tearoff=0)       # tearoff is use for removing deses in menu
last_m.add_command(label="Yes")
last_m.add_command(label="no")

Rendo_M.add_cascade(label="all step",menu=last_m)

editmenu.add_cascade(label="Rendo",menu=Rendo_M)


editmenu.add_separator()    # line border line
# menu 
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Pest")
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Replace")

# ------edit menu end-----------------


root.config(menu=menubar)
root.mainloop()