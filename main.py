import tkinter as tk
import random

root = tk.Tk()
root.title("Rock, Paper, Scissors")

title = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 15), fg="blue")
title.grid(row=0, column=0, pady=5, padx=5)

# Functions
def check_result(user, comp):
    # Rock > Scissor, Scissor > Paper, Paper > Rock

    if user == comp:
        result_label.config(text="Match Draw")
    elif (user == "Rock" and comp == "Scissor") or (user == "Scissor" and comp == "Paper") or (user == "Paper" and comp == "Rock"):
        result_label.config(text="You Win")
    else:
        result_label.config(text="Computer Wins")

def user_choice(choice):
    reset.config(state=tk.NORMAL)
    
    computer_choice = random.choice(["Rock", "Paper", "Scissor"])
    
    rock_btn.config(state=tk.DISABLED)
    paper_btn.config(state=tk.DISABLED)
    scissor_btn.config(state=tk.DISABLED)
    
    player_label.config(text=choice)
    comp_label.config(text=computer_choice)

    check_result(choice, computer_choice)

def reset():
    reset.config(state=tk.DISABLED)    

    rock_btn.config(state=tk.NORMAL)
    paper_btn.config(state=tk.NORMAL)
    scissor_btn.config(state=tk.NORMAL)

    player_label.config(text="Player")
    comp_label.config(text="Computer")
    result_label.config(text="")

# Labels
label_frame = tk.Frame(root)
label_frame.grid(row=1, column=0, pady=5, padx=5)

player_label = tk.Label(label_frame, text="Player", font=("Helvetica", 11))
player_label.grid(row=1, column=0, pady=5, padx=5)

comp_label = tk.Label(label_frame, text="Computer", font=("Helvetica", 11))
comp_label.grid(row=1, column=2, pady=5, padx=5)

vs_label = tk.Label(label_frame, text="VS", font=("Helvetica", 11))
vs_label.grid(row=1, column=1, pady=5, padx=5)

result_label = tk.Label(root, text="", font=("Helvetica", 13), bg="white", width=25, borderwidth=2, relief="solid")
result_label.grid(row=2, column=0, pady=5, padx=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.grid(row=3, column=0, pady=5, padx=5)

rock_btn = tk.Button(btn_frame, text="Rock", font=("Helvetica", 11), command=lambda: user_choice("Rock"))
rock_btn.grid(row=0, column=0, pady=5, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", font=("Helvetica", 11), command=lambda: user_choice("Paper"))
paper_btn.grid(row=0, column=1, pady=5, padx=5)

scissor_btn = tk.Button(btn_frame, text="Scissor", font=("Helvetica", 11), command=lambda: user_choice("Scissor"))
scissor_btn.grid(row=0, column=2, pady=5, padx=5)

reset = tk.Button(root, text="Reset", font=("Helvetica", 11), command=reset)
reset.grid(row=4, column=0, pady=5, padx=5)

reset.config(state=tk.DISABLED)

root.mainloop()
