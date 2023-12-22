from ttkbootstrap import *
import random

root = Window(themename="superhero")
root.geometry("400x400")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
root.title("Guess The Number")

inp_var = IntVar()
chance_var = 20
score_var = 100
random_num = random.randint(1,100)
inp_var.set(0)

def score_updator():
    global score_var
    score_var = chance_var * 5

def chance_updator():
    global chance_var
    chance_var = chance_var - 1

def reset():
    global chance_var
    global random_num
    

    chance_var = 20
    random_num = random.randint(1,100)
    
    score_updator()

    show_chance.config(text=chance_var)
    show_score.config(text=score_var)
    show_hint.config(text="")
    btn.config(text="Guess", command=statment)


def statment():
    global chance_var
    global random_num
    
    chances = chance_var
    inp = inp_var.get()
    randomnum = random_num
    if chances != 0:
        if randomnum == inp:
            score_updator()

            show_chance.config(text=chances)
            show_score.config(text=score_var)
            show_hint.config(text="You Guessed correct Number")
            btn.config(command=reset, bootstyle="sucess")

        elif randomnum > inp:
            score_updator()
            chance_updator()

            show_chance.config(text=chances)
            show_score.config(text=score_var)
            show_hint.config(text="Number is Greater")

        elif randomnum < inp:
            score_updator()
            chance_updator()
            show_chance.config(text=chances)
            show_score.config(text=score_var)
            show_hint.config(text="Number is less")
    else:
        score_updator()
        # chance_var = 0
        # score_var = 0
        show_chance.config(text=00)
        show_score.config(text=00)
        show_hint.config(text="You have no chances")
        btn.config(text="Reset", command=reset, bootstyle="danger")



title_lbl = Label(text="Guess the number Game", font=("lucida", 23), bootstyle="success").pack(padx=5, anchor=N)
score_lbl = Label(text="Score", font=("lucida", 15), bootstyle="primary").pack(anchor=W, padx=25)
chance_lbl = Label(text="Chances", font=("lucida", 15), bootstyle="primary").pack(anchor=W, padx=25, pady=10)

show_score = Label(text=score_var, font=("lucida", 15, "bold"), bootstyle=DANGER)
show_chance = Label(text=chance_var, font=("lucida", 15, "bold"), bootstyle=DANGER)
show_hint = Label(text="Number is less than 100 \n            <100", font=("lucida", 15), bootstyle="primary")

#=================================== Must Edit these values ==================================================== 
show_score.pack(anchor=W, padx=25)
show_chance.pack(anchor=W, padx=25)
show_hint.pack(anchor=N)
#===============================================================================================================
userinp = Entry(textvariable= inp_var).pack()

btn = Button(text="Guess", bootstyle="warning", command=statment)
btn.pack(pady=10)

root.mainloop()