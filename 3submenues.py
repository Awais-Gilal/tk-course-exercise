#Hello AwaisGilal! To create a "Save As" submenu in Tkinter, you can use the following code:

from tkinter import *

def fun():
    print("clicked on button")

root = Tk()
root.title("Menus exercise")
root.geometry("400x400")

# create main menu
main_menu = Menu(root)
root.config(menu=main_menu)

# create file menu
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)

# add options to file menu
file_menu.add_command(label="New", command=fun)
file_menu.add_command(label="Open", command=fun)
file_menu.add_separator()
file_menu.add_command(label="Save", command=fun)

# create "Save As" submenu
save_as_menu = Menu(file_menu, tearoff=False)
file_menu.add_cascade(label="Save As", menu=save_as_menu)

# add options to "Save As" submenu
save_as_menu.add_command(label=".txt", command=fun)
save_as_menu.add_command(label=".py", command=fun)
save_as_menu.add_command(label=".exe", command=fun)
save_as_menu.add_command(label=".bat", command=fun)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# create edit menu
edit_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=edit_menu)

# add options to edit menu
edit_menu.add_command(label="Undo", command=fun)
edit_menu.add_command(label="Redo", command=fun)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=fun)
edit_menu.add_command(label="Copy", command=fun)
edit_menu.add_command(label="Paste", command=fun)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=fun)
edit_menu.add_command(label="Replace", command=fun)

root.mainloop()

#I hope this helps! Let me know if there's anything else I can assist you with.
