import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Python Calculator")

entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=button_equal)
    else:
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", width=10, height=2, font=("Arial", 14), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()
