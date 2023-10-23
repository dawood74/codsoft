import tkinter as tk
from tkinter import ttk
import json

contacts = []

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            loaded_contacts = json.load(file)
            return loaded_contacts
    except FileNotFoundError:
        return []

def save_contacts(filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        list_contacts()
        save_contacts('contacts.json')
        clear_entries()

def list_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_info = f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n"
        contact_list.insert(tk.END, contact_info)
        contact_list.insert(tk.END, '-' * 30 + '\n')

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        if 0 <= selected_index < len(contacts):
            contact = contacts[selected_index]
            name = entry_name.get()
            phone = entry_phone.get()
            email = entry_email.get()
            address = entry_address.get()

            if name and phone:
                contact['Name'] = name
                contact['Phone'] = phone
                contact['Email'] = email
                contact['Address'] = address
                list_contacts()
                save_contacts('contacts.json')
                clear_entries()
        else:
            print("Invalid selection.")
    else:
        print("No contact selected.")

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        if 0 <= selected_index < len(contacts):
            contacts.pop(selected_index)
            list_contacts()
            save_contacts('contacts.json')
        else:
            print("Invalid selection.")
    else:
        print("No contact selected.")

def search_contact():
    query = entry_search.get().strip().lower()
    results = [contact for contact in contacts if query in contact['Name'].lower()]
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_info = f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n"
        contact_list.insert(tk.END, contact_info)
        contact_list.insert(tk.END, '-' * 30 + '\n')

contacts = load_contacts('contacts.json')

root = tk.Tk()
root.title("Contact Book")
root.configure(bg='#1f2937')

style = ttk.Style()
style.configure('Custom.TButton', background='#7289da', foreground='black', font=('Segoe UI', 14), borderwidth=0)
style.map('Custom.TButton', background=[('active', '#5b6ee1')])

frame = tk.Frame(root, bg='#1f2937')
frame.pack(padx=20, pady=20)

label_title = tk.Label(frame, text="Contact Book", fg="white", bg="#1f2937", font=('Segoe UI', 24))
label_title.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

label_name = tk.Label(frame, text="Name:", fg="white", bg="#1f2937", font=('Segoe UI', 12))
label_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")

label_phone = tk.Label(frame, text="Phone:", fg="white", bg="#1f2937", font=('Segoe UI', 12))
label_phone.grid(row=2, column=0, padx=5, pady=5, sticky="w")

label_email = tk.Label(frame, text="Email:", fg="white", bg="#1f2937", font=('Segoe UI', 12))
label_email.grid(row=3, column=0, padx=5, pady=5, sticky="w")

label_address = tk.Label(frame, text="Address:", fg="white", bg="#1f2937", font=('Segoe UI', 12))
label_address.grid(row=4, column=0, padx=5, pady=5, sticky="w")

entry_name = tk.Entry(frame, font=('Segoe UI', 12))
entry_name.grid(row=1, column=1, padx=5, pady=5)

entry_phone = tk.Entry(frame, font=('Segoe UI', 12))
entry_phone.grid(row=2, column=1, padx=5, pady=5)

entry_email = tk.Entry(frame, font=('Segoe UI', 12))
entry_email.grid(row=3, column=1, padx=5, pady=5)

entry_address = tk.Entry(frame, font=('Segoe UI', 12))
entry_address.grid(row=4, column=1, padx=5, pady=5)

add_button = ttk.Button(frame, text="Add Contact", style='Custom.TButton', command=add_contact)
add_button.grid(row=5, column=0, padx=5, pady=10)

update_button = ttk.Button(frame, text="Update Contact", style='Custom.TButton', command=update_contact)
update_button.grid(row=5, column=1, padx=5, pady=10)

search_button = ttk.Button(frame, text="Search Contact", style='Custom.TButton', command=search_contact)
search_button.grid(row=5, column=2, padx=5, pady=10)

delete_button = ttk.Button(frame, text="Delete Contact", style='Custom.TButton', command=delete_contact)
delete_button.grid(row=5, column=3, padx=5, pady=10)

contact_list = tk.Listbox(frame, font=('Segoe UI', 12), bg='#ECECEC', width=45)
contact_list.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label_search = tk.Label(frame, text="Search:", fg="white", bg="#1f2937", font=('Segoe UI', 12))
label_search.grid(row=7, column=0, padx=5, pady=5, sticky="w")

entry_search = tk.Entry(frame, font=('Segoe UI', 12))
entry_search.grid(row=7, column=1, padx=5, pady=5)

list_contacts()

# Calculate the center of the screen more accurately
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
x = (root.winfo_screenwidth() // 3) - (window_width // 4)
y = (root.winfo_screenheight() // 3) - (window_height // 2)

root.geometry(f"+{x}+{y}")

root.mainloop()
