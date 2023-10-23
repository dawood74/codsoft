import tkinter as tk
import random
from tkinter import ttk  # Import the ttk module

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result_label.config(text="You Win!")
        user_score += 1
    else:
        result_label.config(text="Computer Wins!")
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 500) // 2
y = (screen_height - 400) // 2

root.geometry("500x400+{}+{}".format(x, y))

frame = tk.Frame(root, bg='#1f2937')
frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(frame, text="Rock-Paper-Scissors Game", font=("Segoe UI", 16), bg='#1f2937', fg='white')
title_label.pack(pady=10)

user_label = tk.Label(frame, text="Your Choice:", font=("Segoe UI", 12), bg='#1f2937', fg='white')
user_label.pack(padx=10, pady=10, anchor='w')

computer_label = tk.Label(frame, text="Computer's Choice:", font=("Segoe UI", 12), bg='#1f2937', fg='white')
computer_label.pack(padx=10, pady=10, anchor='w')

result_label = tk.Label(frame, text="", font=("Segoe UI", 14, "bold"), bg='#1f2937', fg='white')
result_label.pack(padx=10, pady=10)

user_score_label = tk.Label(frame, text="Your Score: 0", font=("Segoe UI", 12), bg='#1f2937', fg='white')
user_score_label.pack(padx=10, pady=10, anchor='w')

computer_score_label = tk.Label(frame, text="Computer's Score: 0", font=("Segoe UI", 12), bg='#1f2937', fg='white')
computer_score_label.pack(padx=10, pady=10, anchor='w')

button_frame = tk.Frame(frame, bg='#1f2937')
button_frame.pack()

# Create a style and configure the button style
style = ttk.Style()
style.configure('Custom.TButton', background='#7289da', foreground='black', font=('Segoe UI', 14), borderwidth=0)
style.map('Custom.TButton', background=[('active', '#5b6ee1')])

rock_button = ttk.Button(button_frame, text="Rock", style='Custom.TButton', command=lambda: play_game("Rock"))
rock_button.pack(side='left', padx=5, pady=10)

paper_button = ttk.Button(button_frame, text="Paper", style='Custom.TButton', command=lambda: play_game("Paper"))
paper_button.pack(side='left', padx=5, pady=10)

scissors_button = ttk.Button(button_frame, text="Scissors", style='Custom.TButton', command=lambda: play_game("Scissors"))
scissors_button.pack(side='left', padx=5, pady=10)

root.mainloop()
