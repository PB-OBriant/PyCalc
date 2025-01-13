import tkinter as tk
import math

# Initialize the expression string
expression = ""

# Function to handle button clicks
def button_click(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the expression
def evaluate_expression(event=None): # event=None allows the function to be called without an event
    global expression
    expression = entry.get()
    try:
        result = eval(expression, {"__builtins__": None}, {"math": math})
        result_label.config(text=f"Result: {result}")
        expression = str(result)
    except Exception as e:
        result_label.config(text=f"Error: {e}")
        expression = ""

# Function to clear the entry and result label
def clear_all():
    global expression
    expression = ""
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.config(bg="black")

# Bind the Enter key to the evaluate_expression function
root.bind('<Return>', evaluate_expression)

# Create a single entry field for numbers
entry = tk.Entry(root, width=20, bg="gray", fg='white')
entry.grid(row=0, column=1, columnspan=5, padx=5, pady=5)

# Create buttons for operations
tk.Button(root, text="Add", command=lambda: button_click("+"), bg="black", fg='white').grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="Subtract", command=lambda: button_click("-"), bg="black", fg='white').grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Multiply", command=lambda: button_click("*"), bg="black", fg='white').grid(row=1, column=2, padx=5, pady=5)
tk.Button(root, text="Divide", command=lambda: button_click("/"), bg="black", fg='white').grid(row=1, column=3, padx=5, pady=5)

# Create a button to evaluate the expression
tk.Button(root, text="Calculate", command=evaluate_expression, bg="black", fg='white').grid(row=7, column=0, columnspan=4, padx=5, pady=5)

# Create a button to clear the expression and result
tk.Button(root, text="Clear", command=clear_all, bg="black", fg='white').grid(row=7, column=3, padx=5, pady=5)

# Create buttons for number input
tk.Button(root, text="1", command=lambda: button_click("1"), bg="black", fg='white').grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="2", command=lambda: button_click("2"), bg="black", fg='white').grid(row=3, column=2, padx=5, pady=5)
tk.Button(root, text="3", command=lambda: button_click("3"), bg="black", fg='white').grid(row=3, column=3, padx=5, pady=5)
tk.Button(root, text="4", command=lambda: button_click("4"), bg="black", fg='white').grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="5", command=lambda: button_click("5"), bg="black", fg='white').grid(row=4, column=2, padx=5, pady=5)
tk.Button(root, text="6", command=lambda: button_click("6"), bg="black", fg='white').grid(row=4, column=3, padx=5, pady=5)
tk.Button(root, text="7", command=lambda: button_click("7"), bg="black", fg='white').grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="8", command=lambda: button_click("8"), bg="black", fg='white').grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="9", command=lambda: button_click("9"), bg="black", fg='white').grid(row=5, column=3, padx=5, pady=5)
tk.Button(root, text="0", command=lambda: button_click("0"), bg="black", fg='white').grid(row=6, column=2, padx=5, pady=5)
tk.Button(root, text=".", command=lambda: button_click("."), bg="black", fg='white').grid(row=6, column=3, padx=5, pady=5)

# Create a label to display results
result_label = tk.Label(root, text="Result: ", width=20, bg="black", fg='white')
result_label.grid(row=8, column=1, columnspan=5, padx=5, pady=5)

# Run application
root.mainloop()
