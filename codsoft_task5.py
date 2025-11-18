import tkinter as tk
from tkinter import messagebox
contacts = [
    {"name":"Rohit Sharma","phone":"9876543210","email":"rohit@example.com","address":"Mumbai"},
    {"name":"Priya Verma","phone":"9123456780","email":"priya@example.com","address":"Delhi"},
    {"name":"Adithya","phone":"9000001122","email":"adithya@example.com","address":"Chennai"},
    {"name":"Karan Patel","phone":"9090909090","email":"karan@example.com","address":"Hyderabad"}
]

filtered = []

def refresh_list(items=None):
    listbox.delete(0, tk.END)
    data = items if items is not None else contacts
    for c in data:
        listbox.insert(tk.END, f"{c['name']} - {c['phone']}")

def fill_fields(event=None):
    try:
        i = listbox.curselection()[0]
        c = contacts[i]
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_name.insert(0, c["name"])
        entry_phone.insert(0, c["phone"])
        entry_email.insert(0, c["email"])
        entry_address.insert(0, c["address"])
    except:
        pass

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    if not name or not phone:
        messagebox.showwarning("Warning", "Name and phone are required.")
        return
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    clear_fields()
    refresh_list()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def delete_contact():
    try:
        i = listbox.curselection()[0]
    except:
        messagebox.showwarning("Warning", "Select a contact to delete.")
        return
    contacts.pop(i)
    refresh_list()
    clear_fields()

def update_contact():
    try:
        i = listbox.curselection()[0]
        c = contacts[i]
    except:
        messagebox.showwarning("Warning", "Select a contact to update.")
        return
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    if not name or not phone:
        messagebox.showwarning("Warning", "Name and phone cannot be empty.")
        return
    contacts[i] = {"name": name, "phone": phone, "email": email, "address": address}
    refresh_list()

def live_search(event=None):
    q = search_entry.get().lower().strip()
    if not q:
        refresh_list()
        return
    filtered = [c for c in contacts if q in c["name"].lower() or q in c["phone"]]
    refresh_list(filtered)

root = tk.Tk()
root.title("Contact Book")
root.geometry("520x620")
root.configure(bg="#f0f7ff")

title = tk.Label(root, text="📘 Contact Book", font=("Arial", 22, "bold"), bg="#f0f7ff", fg="#0059b3")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f7ff")
frame.pack(pady=5)

tk.Label(frame, text="Name:", font=("Arial", 12), bg="#f0f7ff").grid(row=0, column=0, sticky="e", pady=3)
entry_name = tk.Entry(frame, width=32, font=("Arial", 12))
entry_name.grid(row=0, column=1, pady=3)

tk.Label(frame, text="Phone:", font=("Arial", 12), bg="#f0f7ff").grid(row=1, column=0, sticky="e", pady=3)
entry_phone = tk.Entry(frame, width=32, font=("Arial", 12))
entry_phone.grid(row=1, column=1, pady=3)

tk.Label(frame, text="Email:", font=("Arial", 12), bg="#f0f7ff").grid(row=2, column=0, sticky="e", pady=3)
entry_email = tk.Entry(frame, width=32, font=("Arial", 12))
entry_email.grid(row=2, column=1, pady=3)

tk.Label(frame, text="Address:", font=("Arial", 12), bg="#f0f7ff").grid(row=3, column=0, sticky="ne", pady=3)
entry_address = tk.Entry(frame, width=32, font=("Arial", 12))
entry_address.grid(row=3, column=1, pady=3)

btn_frame = tk.Frame(root, bg="#f0f7ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=14, height=1, bg="#4da6ff", fg="white", font=("Arial", 11), command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=14, height=1, bg="#3385ff", fg="white", font=("Arial", 11), command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=14, height=1, bg="#ff5c33", fg="white", font=("Arial", 11), command=delete_contact).grid(row=0, column=2, padx=5)

search_label = tk.Label(root, text="Search:", font=("Arial", 12), bg="#f0f7ff")
search_label.pack()
search_entry = tk.Entry(root, width=40, font=("Arial", 12))
search_entry.pack(pady=5)
search_entry.bind("<KeyRelease>", live_search)

listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12))
listbox.pack(pady=15)
listbox.bind("<<ListboxSelect>>", fill_fields)

refresh_list()
root.mainloop()