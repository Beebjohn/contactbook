import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.populate_listbox()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            self.contacts[name] = phone
            self.populate_listbox()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter name and phone number.")

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.listbox.insert(tk.END, f"{name}: {phone}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
