import tkinter as tk
import random

root = tk.Tk()
root.title("Rock, Paper, Scissors")

title = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 15), fg="blue")
title.grid(row=0, column=0, pady=5, padx=5)

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

rock_btn = tk.Button(btn_frame, text="Rock", font=("Helvetica", 11))
rock_btn.grid(row=0, column=0, pady=5, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", font=("Helvetica", 11))
paper_btn.grid(row=0, column=1, pady=5, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissor", font=("Helvetica", 11))
scissors_btn.grid(row=0, column=2, pady=5, padx=5)

root.mainloop()