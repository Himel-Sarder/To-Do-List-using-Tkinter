from tkinter import *


def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        pass

root = Tk()
root.title("Python To-Do List")
root.geometry("300x350")  # Set the window size

# Set the background color to yellow
root.configure(bg="#138086")

# Status Title Label
status_label = Label(root, text="To-Do List", font=("Arial", 14, "bold"), bg="#138086", fg="white")
status_label.pack(pady=10)

# Widgets
entry = Entry(root)
addButton = Button(root, text="Add Task", bg="black", fg="white", command=add_task)
listbox = Listbox(root)
delButton = Button(root, text="Delete Task", bg="black", fg="white", command=delete_task)

# GUI Layout with separation
entry.pack(pady=5)
addButton.pack(pady=5, padx=10)  # Added padx for separation
listbox.pack(pady=5)
delButton.pack(pady=5)

root.mainloop()