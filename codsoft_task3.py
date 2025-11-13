import tkinter as tk
from tkinter import ttk, messagebox
import random, string

def set_level(level):
    try:
        total = int(total_entry.get())
    except:
        messagebox.showwarning("Warning error", "Enter total length first to ensure correctness.")
        return

    if level == "Easy":
        upper_entry.delete(0, tk.END)
        lower_entry.delete(0, tk.END)
        digit_entry.delete(0, tk.END)
        symbol_entry.delete(0, tk.END)
        upper_entry.insert(0, total//4)
        lower_entry.insert(0, total//2)
        digit_entry.insert(0, total - (total//4 + total//2))
        symbol_entry.insert(0, 0)

    elif level == "Medium":
        upper_entry.delete(0, tk.END)
        lower_entry.delete(0, tk.END)
        digit_entry.delete(0, tk.END)
        symbol_entry.delete(0, tk.END)
        upper_entry.insert(0, total//4)
        lower_entry.insert(0, total//4)
        digit_entry.insert(0, total//4)
        symbol_entry.insert(0, total - (3*(total//4)))

    elif level == "Hard":
        upper_entry.delete(0, tk.END)
        lower_entry.delete(0, tk.END)
        digit_entry.delete(0, tk.END)
        symbol_entry.delete(0, tk.END)
        upper_entry.insert(0, total//4)
        lower_entry.insert(0, total//4 + (total % 2))
        digit_entry.insert(0, total//4)
        symbol_entry.insert(0, total - (upper_entry.get().isnumeric() and lower_entry.get().isnumeric() and digit_entry.get().isnumeric()))

def generate_password():
    try:
        total = int(total_entry.get())
        upper = int(upper_entry.get())
        lower = int(lower_entry.get())
        digit = int(digit_entry.get())
        symbol = int(symbol_entry.get())
    except:
        messagebox.showwarning("Warning", "Enter valid numbers.")
        return

    if upper + lower + digit + symbol != total:
        messagebox.showwarning("Warning", "Please ensure the character counts match the total password length.")
        return

    password_chars = []
    password_chars += random.choices(string.ascii_uppercase, k=upper)
    password_chars += random.choices(string.ascii_lowercase, k=lower)
    password_chars += random.choices(string.digits, k=digit)
    password_chars += random.choices(string.punctuation, k=symbol)
    random.shuffle(password_chars)

    generated_password.set("".join(password_chars))

def copy_password():
    pw = generated_password.get()
    if pw:
        root.clipboard_clear()
        root.clipboard_append(pw)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("360x370")

tk.Label(root, text="Total Password Length:").pack()
total_entry = tk.Entry(root)
total_entry.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="UPPERCASE:").grid(row=0, column=0)
upper_entry = tk.Entry(frame, width=5)
upper_entry.grid(row=0, column=1)

tk.Label(frame, text="lowercase:").grid(row=1, column=0)
lower_entry = tk.Entry(frame, width=5)
lower_entry.grid(row=1, column=1)

tk.Label(frame, text="digits:").grid(row=2, column=0)
digit_entry = tk.Entry(frame, width=5)
digit_entry.grid(row=2, column=1)

tk.Label(frame, text="symbols:").grid(row=3, column=0)
symbol_entry = tk.Entry(frame, width=5)
symbol_entry.grid(row=3, column=1)

tk.Label(root, text="Difficulty:").pack()
tk.Button(root, text="Easy", command=lambda: set_level("Easy")).pack()
tk.Button(root, text="Medium", command=lambda: set_level("Medium")).pack()
tk.Button(root, text="Hard", command=lambda: set_level("Hard")).pack()

generated_password = tk.StringVar()
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=generated_password, width=30, justify="center").pack()

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)
root.mainloop()