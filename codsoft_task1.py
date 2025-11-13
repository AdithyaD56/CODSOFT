import tkinter as tk
from tkinter import messagebox, simpledialog
import json, os

STORE = "tasks.json"
tasks = []

def load():
    global tasks
    if os.path.exists(STORE):
        with open(STORE,"r") as f:
            tasks = json.load(f)

def save():
    with open(STORE,"w") as f:
        json.dump(tasks,f,indent=2)

def display():
    listbox.delete(0, tk.END)
    sorted_tasks = sorted(tasks, key=lambda x: x["done"])
    for t in sorted_tasks:
        mark = "✓" if t["done"] else "•"
        listbox.insert(tk.END, f"[{mark}] {t['name']}")

def add_task():
    name = entry.get().strip()
    if not name:
        messagebox.showwarning("Warning","Enter a task.")
        return
    tasks.append({"name":name,"done":False})
    entry.delete(0, tk.END)
    save()
    display()

def edit_task():
    sorted_tasks = sorted(tasks, key=lambda x: x["done"])
    try:
        index = listbox.curselection()[0]
        task_to_edit = sorted_tasks[index]
    except:
        messagebox.showwarning("Warning","Select a task to edit.")
        return
    new = simpledialog.askstring("Edit Task","Update task:", initialvalue=task_to_edit["name"])
    if new and new.strip():
        for t in tasks:
            if t["name"] == task_to_edit["name"] and t["done"] == task_to_edit["done"]:
                t["name"] = new.strip()
                break
        save()
        display()

def mark_completed():
    sorted_tasks = sorted(tasks, key=lambda x: x["done"])
    try:
        index = listbox.curselection()[0]
        task = sorted_tasks[index]
    except:
        messagebox.showwarning("Warning","Select a task.")
        return
    for t in tasks:
        if t == task:
            t["done"] = True
            break
    save()
    display()

def mark_pending():
    sorted_tasks = sorted(tasks, key=lambda x: x["done"])
    try:
        index = listbox.curselection()[0]
        task = sorted_tasks[index]
    except:
        messagebox.showwarning("Warning","Select a task.")
        return
    for t in tasks:
        if t == task:
            t["done"] = False
            break
    save()
    display()

def delete_task():
    sorted_tasks = sorted(tasks, key=lambda x: x["done"])
    try:
        index = listbox.curselection()[0]
        task = sorted_tasks[index]
    except:
        messagebox.showwarning("Warning","Select a task to delete.")
        return
    tasks.remove(task)
    save()
    display()

def clear_tasks():
    tasks.clear()
    save()
    display()

root = tk.Tk()
root.title("To-Do List")
root.geometry("420x460")

entry = tk.Entry(root, width=28, font=("Arial",14))
entry.pack(pady=10)
btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="Add", width=10, command=add_task).grid(row=0, column=0, padx=3)
tk.Button(btn_frame, text="Edit", width=10, command=edit_task).grid(row=0, column=1, padx=3)
tk.Button(btn_frame, text="Mark Completed", width=15, command=mark_completed).grid(row=0, column=2, padx=3)
tk.Button(btn_frame, text="Mark Pending", width=15, command=mark_pending).grid(row=0, column=3, padx=3)
listbox = tk.Listbox(root, width=40, height=12, font=("Arial",12))
listbox.pack(pady=10)
tk.Button(root, text="Delete Task", width=18, command=delete_task).pack(pady=3)
tk.Button(root, text="Clear All", width=18, command=clear_tasks).pack(pady=3)
load()
display()
root.mainloop()