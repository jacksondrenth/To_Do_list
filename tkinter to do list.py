import tkinter as tk

root = tk.Tk()


# functions
def add_to_list():
    text = entry.get()
    listbox.insert(tk.END, text)
    entry.delete(0, tk.END)


def remove_items():
    try:
        selection = list(listbox.curselection())[::-1]
        for index in selection:
            listbox.delete(index)
    except IndexError:
        pass


def on_close():
    with open('todo_list.txt', 'w') as f:
        listbox_items = listbox.get(0, 'end')
        for item in listbox_items:
            f.write(item + '\n')
    root.destroy()


# label
label = tk.Label(root, text="To Do List")
label.pack()
# entry box
entry = tk.Entry(root)
entry.pack()

# add button
button = tk.Button(root, text='Add to To Do List', command=add_to_list)
button.pack()

# listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

# delete button
remove_button = tk.Button(root, text="remove", command=remove_items)
remove_button.pack()

try:
    # Open the file in read mode ('r')
    with open('todo_list.txt', 'r') as f:
        lines = f.readlines()
        # Add each line to the listbox
        for line in lines:
            # Strip off the newline character at the end of the line before adding it to the listbox
            listbox.insert('end', line.strip())
except FileNotFoundError:
    # If the file doesn't exist, skip loading the tasks.
    # The file will be created when you save for the first time.
    pass

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
