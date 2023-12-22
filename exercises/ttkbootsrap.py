from ttkbootstrap import *
# from tkinter import *
def check():
    lbl.config(text="checked")
root = Window(themename="superhero")
# root = Tk()
root.title("bootstraper")
root.geometry("500x500")

lbl = Label(text="Hellow bootstrap", font=('lucida', 23, 'bold'))
lbl.pack(padx=23, pady=23)

Button(text="check", command=check).pack()
root.mainloop()