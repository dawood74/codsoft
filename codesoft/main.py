import tkinter as tk
from tkinter import ttk
import os

def print_message(message):
    print(message)

def toodlist():
    os.system('todolist.py')

# Function to open gun.py file
def CALCULATOR():
    os.system('calc.py')

def passwordgen():
    os.system('passowrd.py')

def rockpaper():
    os.system('game.py')

def contactbook():
    os.system('contactbook.py')

# Create the main window
window = tk.Tk()
window.title("My Form")

# Calculate the position to center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 800
window_height = 720
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg='#1f2937')

# Create a frame to hold the buttons
frame = tk.Frame(window, bg='#1f2937')
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a custom button style
style = ttk.Style()
style.configure('Custom.TButton', background='#7289da', foreground='black', font=('Segoe UI', 14), borderwidth=0)
style.map('Custom.TButton', background=[('active', '#5b6ee1')])

# Create the buttons with the custom style
button1 = ttk.Button(frame, text="TO DO LIST", style='Custom.TButton', command=toodlist)
button2 = ttk.Button(frame, text="CALCULATOR", style='Custom.TButton', command=CALCULATOR)
button3 = ttk.Button(frame, text="PASSWORD GENERATOR", style='Custom.TButton', command=passwordgen)
button4 = ttk.Button(frame, text="Rock-Paper-Scissors Game", style='Custom.TButton', command=rockpaper)
button5 = ttk.Button(frame, text="Contact Book", style='Custom.TButton', command=contactbook)

# Add the buttons to the frame with modified size and padding using grid
button1.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=10)
button2.grid(row=0, column=1, padx=20, pady=20, ipadx=20, ipady=10)
button3.grid(row=0, column=2, padx=20, pady=20, ipadx=20, ipady=10)
button4.grid(row=1, column=0, padx=20, pady=20, ipadx=20, ipady=10)
button5.grid(row=1, column=1, padx=20, pady=20, ipadx=20, ipady=10)

# Add a title to the top middle of the form
title_label = tk.Label(window, text="CodSoft Tasks", font=('Segoe UI', 24), bg='#1f2937', fg='white')
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Start the main event loop
window.mainloop()
