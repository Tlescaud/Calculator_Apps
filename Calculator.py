# importing the necessary libraries

# upload code to github...share github link with Nerry once change calculator to a scientic calculator....



import tkinter as tk

import math

def on_click(button_text):
    if button_text == "=":
        try:
            result.set(str(eval(entry.get())))
        except:
            result.set("Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Initialize window
root = tk.Tk()
root.title("Calculator")

# Input field
entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16)).grid(row=1, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
    ('C', 6, 0)
]

# Create buttons
for text, row, col in buttons:
    tk.Button(root, text=text, font=("Arial", 16), command=lambda t=text: on_click(t)).grid(row=row, column=col)

root.mainloop()

# Second calculator adding scientific functions

import tkinter as tk
import math

def on_click(button_text):
    if button_text == "=":
        try:
            result.set(str(eval(entry.get(), {"math": math})))  # Securely evaluating using math module
        except:
            result.set("Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text in ["sqrt", "log", "sin", "cos", "tan"]:
        try:
            value = float(entry.get())
            if button_text == "sqrt":
                result.set(str(math.sqrt(value)))
            elif button_text == "log":
                result.set(str(math.log(value)))
            elif button_text == "sin":
                result.set(str(math.sin(math.radians(value))))
            elif button_text == "cos":
                result.set(str(math.cos(math.radians(value))))
            elif button_text == "tan":
                result.set(str(math.tan(math.radians(value))))
        except:
            result.set("Error")
    else:
        entry.insert(tk.END, button_text)

# Initialize window
root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=5)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16)).grid(row=1, column=0, columnspan=5)

# Button layout for scientific mode
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('sqrt', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('log', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('sin', 4, 4),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('cos', 5, 4),
    ('C', 6, 0), ('(', 6, 1), (')', 6, 2), ('^', 6, 3), ('tan', 6, 4)
]

for text, row, col in buttons:
    tk.Button(root, text=text, font=("Arial", 16), command=lambda t=text: on_click(t)).grid(row=row, column=col)

root.mainloop()





