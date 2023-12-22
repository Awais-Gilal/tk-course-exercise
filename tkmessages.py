from tkinter import *

import tkinter.messagebox as tmsg

def fun():
    print("clicked on menue button: ")



root = Tk()
root.title("Menues & Messages boxe")
root.geometry("600x300")

mainmenu = Menu(root, tearoff=False)

root.config(menu=mainmenu)

#=============file menu ==================
file = Menu(mainmenu, tearoff=False)
file.add_command(label="New", command=fun)
file.add_command(label="Open", command=fun)
file.add_separator()
file.add_command(label="Save", command=fun)
mainmenu.add_cascade(label="File", menu=file)

#===============save as menu===============
save_as_menu = Menu(file, tearoff=False)
save_as_menu.add_command(label=".txt", command=fun)
save_as_menu.add_command(label=".py", command=fun)
save_as_menu.add_command(label=".xml", command=fun)
save_as_menu.add_command(label=".bat", command=fun)
file.add_cascade(label="Save As", menu=save_as_menu)

file.add_separator()
file.add_command(label="Exit", command=quit)

#===================Edit=====================
edit = Menu(mainmenu, tearoff=False)
edit.add_command(label="Unod", command=fun)
edit.add_command(label="Redo", command=fun)
edit.add_separator()
edit.add_command(label="Cut", command=fun)
edit.add_command(label="Copy", command=fun)
edit.add_command(label="Paste", command=fun)
edit.add_separator()
edit.add_command(label="Find", command=fun)
edit.add_command(label="Replace", command=fun)
mainmenu.add_cascade(label="Edit", menu=edit)


#====================funcions====================
def box():
    print("clicked on the help fuchtion")
    a = tmsg.askquestion("Clicked", "this is dialog box")
    print(a)
#==================== Help menu =================
help = Menu(mainmenu, tearoff=False)
help.add_command(label="Help", command=box)
mainmenu.add_cascade(label="help", menu=help)
root.mainloop()