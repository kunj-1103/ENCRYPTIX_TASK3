import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, width=5)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=lambda: password_entry.delete(0, tk.END) or password_entry.insert(0, generate_password(int(length_entry.get()))))
generate_button.pack()

password_entry = tk.Entry(root, width=20)
password_entry.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_password)
copy_button.pack()

root.mainloop()
