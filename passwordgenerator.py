import tkinter as tk
import random
import string
def generate_password():
    password_length = int(password_length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    generated_password.set(password)
def reset_fields():
    username_entry.delete(0, tk.END)
    password_length_entry.delete(0, tk.END)
    generated_password.set("")
root = tk.Tk()
root.title("Password Generator")
username_label = tk.Label(root, text="Enter User Name:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()
password_length_label = tk.Label(root, text="Enter Password Length:")
password_length_label.pack()
password_length_entry = tk.Entry(root)
password_length_entry.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()
generated_password = tk.StringVar()
generated_password_label = tk.Label(root, text="Generated Password:")
generated_password_label.pack()
generated_password_display = tk.Label(root, textvariable=generated_password)
generated_password_display.pack()
accept_button = tk.Button(root, text="Accept", command=root.quit)
accept_button.pack()
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack()
root.mainloop()
