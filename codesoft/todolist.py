import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
from datetime import datetime

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            for task in tasks:
                task.setdefault('additional_info', '')  # Ensure 'additional_info' exists for each task
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = task_entry.get()
    if title:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append({'title': title, 'status': 'Incomplete', 'time_added': current_time, 'additional_info': '', 'completed': False})
        list_tasks()
        save_tasks(filename, tasks)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Task title cannot be empty")

def update_task():
    selected_index = task_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_title = simpledialog.askstring("Update Task", "Enter a new title:")
        if new_title:
            tasks[selected_index] = {
                'title': new_title,
                'status': tasks[selected_index]['status'],
                'time_added': tasks[selected_index]['time_added'],
                'additional_info': tasks[selected_index]['additional_info'],
                'completed': tasks[selected_index].get('completed', False)
            }
            list_tasks()
            save_tasks(filename, tasks)
    else:
        messagebox.showerror("Error", "Select a task to update.")

def complete_task():
    selected_index = task_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        tasks[selected_index]['status'] = 'Completed'
        tasks[selected_index]['completed'] = True
        list_tasks()
        save_tasks(filename, tasks)
    else:
        messagebox.showerror("Error", "Select a task to mark as complete.")

def delete_task():
    selected_index = task_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del tasks[selected_index]
        list_tasks()
        save_tasks(filename, tasks)
    else:
        messagebox.showerror("Error", "Select a task to delete.")

def open_note_window():
    selected_index = task_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        note_window = tk.Toplevel()
        note_window.title("Task Note")

        note_window.geometry("400x250")
        note_window.configure(bg='#1f2937')

        additional_info_label = tk.Label(note_window, text="Additional Information:", font=('Segoe UI', 12), bg='#1f2937', fg='white')
        additional_info_label.pack(padx=10, pady=10)

        additional_info = tasks[selected_index].get('additional_info', '')

        additional_info_text = tk.Text(note_window, font=('Segoe UI', 12), height=5, width=40)
        additional_info_text.insert(tk.END, additional_info)
        additional_info_text.pack(padx=10, pady=10)

        def save_note():
            tasks[selected_index]['additional_info'] = additional_info_text.get("1.0", "end-1c")
            save_tasks(filename, tasks)
            note_window.destroy()

        style = ttk.Style()
        style.configure('Custom.TButton', background='#7289da', foreground='black', font=('Segoe UI', 14), borderwidth=0)
        style.map('Custom.TButton', background=[('active', '#5b6ee1')])

        save_button = ttk.Button(note_window, text="Save", command=save_note, style='Custom.TButton')
        save_button.pack(padx=10, pady=10)

        screen_width = note_window.winfo_screenwidth()
        screen_height = note_window.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 250) // 2
        note_window.geometry(f"400x250+{x}+{y}")

def list_tasks():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        completed = "✔" if task.get('completed', False) else ""
        task_list.insert(tk.END, f"{completed} {task['title']} - {task['status']} (Added: {task['time_added']})")

def main():
    global tasks, filename, task_entry, task_list
    filename = 'tasks.json'
    tasks = load_tasks(filename)

    root = tk.Tk()
    root.title("To-Do List")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 500) // 2
    y = (screen_height - 450) // 2
    root.geometry(f"500x450+{x}+{y}")
    root.configure(bg='#1f2937')

    frame = tk.Frame(root, bg='#1f2937')
    frame.pack(fill=tk.BOTH, expand=True)

    task_label = tk.Label(frame, text="Task:", bg='#1f2937', fg='white', font=('Segoe UI', 12))
    task_label.grid(row=0, column=0, padx=10, pady=10)

    task_entry = tk.Entry(frame, font=('Segoe UI', 12))
    task_entry.grid(row=0, column=1, padx=10, pady=10)

    style = ttk.Style()
    style.configure('Custom.TButton', background='#7289da', foreground='black', font=('Segoe UI', 14), borderwidth=0)
    style.map('Custom.TButton', background=[('active', '#5b6ee1')])

    add_button = ttk.Button(frame, text="Add Task", command=add_task, style='Custom.TButton')
    add_button.grid(row=0, column=2, padx=10, pady=10)

    update_button = ttk.Button(frame, text="Update Task", command=update_task, style='Custom.TButton')
    update_button.grid(row=1, column=0, padx=10, pady=10)

    complete_button = ttk.Button(frame, text="Complete Task", command=complete_task, style='Custom.TButton')
    complete_button.grid(row=1, column=1, padx=10, pady=10)

    delete_button = ttk.Button(frame, text="Delete Task", command=delete_task, style='Custom.TButton')
    delete_button.grid(row=1, column=2, padx=10, pady=10)

    #note_button = ttk.Button(frame, text="Add Note", command=open_note_window, style='Custom.TButton')
    #note_button.grid(row=2, column=0, padx=10, pady=10)

    task_list = tk.Listbox(frame, font=('Segoe UI', 12), bg='#ECECEC')
    task_list.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    task_list.bind('<Double-Button-1>', lambda event: open_note_window())

    list_tasks()

    root.mainloop()

if __name__ == "__main__":
    main()
