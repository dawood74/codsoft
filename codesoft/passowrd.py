import tkinter as tk
from tkinter import ttk
import secrets
import string

def generate_password():
    length = int(password_length.get())
    
    if length < 6:
        error_label.config(text="Password length must be at least 6 characters", fg='red')
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        generated_password.set(password)
        error_label.config(text="")
        password_label.config(fg='#2ecc71')  # Light green color

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")  # Increased the window height to accommodate the tips and space
root.configure(bg='#1f2937')

frame = tk.Frame(root, bg='#1f2937')
frame.pack(fill=tk.BOTH, expand=True)

# Add tips labels with space between each tip
tips_text = "Tips for a good password:\n\n"\
            "1. Use at least 6 characters.\n"\
            "2. Include a mix of uppercase and lowercase letters.\n"\
            "3. Use numbers and symbols for extra security.\n\n"

tips_label = tk.Label(frame, text=tips_text, bg='#1f2937', fg='white', font=('Segoe UI', 12), justify="left")
tips_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

label = tk.Label(frame, text="Password Length:", bg='#1f2937', fg='white', font=('Segoe UI', 12))
label.grid(row=1, column=0, padx=10, pady=10)

password_length = tk.Entry(frame, font=('Segoe UI', 12))
password_length.grid(row=1, column=1, padx=10, pady=10)

style = ttk.Style()
style.configure('Custom.TButton', background='#7289da', foreground='black', font=('Segoe UI', 14), borderwidth=0)
style.map('Custom.TButton', background=[('active', '#5b6ee1')])

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password, style='Custom.TButton')
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

generated_password = tk.StringVar()
password_label = tk.Label(frame, textvariable=generated_password, bg='#1f2937', fg='#2ecc71', font=('Segoe UI', 12))  # Light green color
password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

error_label = tk.Label(frame, text="", bg='#1f2937', fg='red', font=('Segoe UI', 12))
error_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 400) // 2
y = (screen_height - 400) // 2
root.geometry(f"400x400+{x}+{y}")

root.mainloop()
