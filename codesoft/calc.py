import tkinter as tk
from tkinter import ttk

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_choice.get()

        if operation == "Add":
            result.set(num1 + num2)
        elif operation == "Subtract":
            result.set(num1 - num2)
        elif operation == "Multiply":
            result.set(num1 * num2)
        elif operation == "Divide":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Division by zero")
    except ValueError:
        result.set("Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 500) // 2
y = (screen_height - 300) // 2
root.geometry(f"600x300+{x}+{y}")

frame = tk.Frame(root, bg='#1f2937')
frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(frame, text="Simple Calculator", font=('Segoe UI', 16), background='#1f2937', foreground='white')
title_label.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

title_num1 = ttk.Label(frame, text="Number 1:", font=('Segoe UI', 12), background='#1f2937', foreground='white')
title_num1.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_num1 = ttk.Entry(frame, font=('Segoe UI', 12))
entry_num1.grid(row=1, column=1, padx=5, pady=5)

title_operation = ttk.Label(frame, text="Operation:", font=('Segoe UI', 12), background='#1f2937', foreground='white')
title_operation.grid(row=1, column=2, padx=5, pady=5, sticky="e")

operation_choice = ttk.Combobox(frame, values=["Add", "Subtract", "Multiply", "Divide"], font=('Segoe UI', 12))
operation_choice.grid(row=1, column=3, padx=5, pady=5)
operation_choice.set("Add")

title_num2 = ttk.Label(frame, text="Number 2:", font=('Segoe UI', 12), background='#1f2937', foreground='white')
title_num2.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_num2 = ttk.Entry(frame, font=('Segoe UI', 12))
entry_num2.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate", command=perform_calculation, style='Custom.TButton')
calculate_button.grid(row=2, column=3, padx=5, pady=5)

result = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result, font=('Segoe UI', 14))
result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
