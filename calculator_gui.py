import customtkinter as ctk
import math

# Initialize the expression string
expression = ""

# Function to handle button clicks
def button_click(value):
    global expression
    expression += str(value)
    entry.delete(0, ctk.END)
    entry.insert(ctk.END, expression)

# Function to evaluate the expression
def evaluate_expression(event=None): # event=None allows the function to be called without an event
    global expression
    expression = entry.get()
    try:
        result = eval(expression, {"__builtins__": None}, {"math": math})
        # round to 10 decimal places
        result = round(result, 10)
        result_label.configure(text=f"Result: {result}")
        expression = str(result)
    except Exception as e:
        result_label.configure(text=f"Error: {e}")
        expression = ""

# Function to clear the entry and result label
def clear_all():
    global expression
    expression = ""
    entry.delete(0, ctk.END)
    result_label.configure(text="Result: ")

# Create application window
root = ctk.CTk()
root.title("Calculator")
root.geometry("600x400")
root.configure(bg="black")

# Bind the Enter key to the evaluate_expression function
root.bind('<Return>', evaluate_expression)

# Create a single entry field for numbers
entry = ctk.CTkEntry(root, width=200, bg_color="gray", fg_color='black')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create buttons for operations
ctk.CTkButton(root, text="Add", command=lambda: button_click("+"), bg_color="black", fg_color='black').grid(row=1, column=0, padx=5, pady=5)
ctk.CTkButton(root, text="Subtract", command=lambda: button_click("-"), bg_color="black", fg_color='black').grid(row=1, column=1, padx=5, pady=5)
ctk.CTkButton(root, text="Multiply", command=lambda: button_click("*"), bg_color="black", fg_color='black').grid(row=1, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="Divide", command=lambda: button_click("/"), bg_color="black", fg_color='black').grid(row=1, column=3, padx=5, pady=5)
ctk.CTkButton(root, text="Power", command=lambda: button_click("**"), bg_color="black", fg_color='black').grid(row=2, column=0, padx=5, pady=5)
ctk.CTkButton(root, text="Square Root", command=lambda: button_click("math.sqrt("), bg_color="black", fg_color='black').grid(row=2, column=1, padx=5, pady=5)

# Trig Operations
ctk.CTkButton(root, text="Sine", command=lambda: button_click("math.sin("), bg_color="black", fg_color='black').grid(row=2, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="Cosine", command=lambda: button_click("math.cos("), bg_color="black", fg_color='black').grid(row=2, column=3, padx=5, pady=5)
ctk.CTkButton(root, text="Tangent", command=lambda: button_click("math.tan("), bg_color="black", fg_color='black').grid(row=3, column=0, padx=5, pady=5)
ctk.CTkButton(root, text="Arcsine", command=lambda: button_click("math.asin("), bg_color="black", fg_color='black').grid(row=3, column=1, padx=5, pady=5)
ctk.CTkButton(root, text="Arccosine", command=lambda: button_click("math.acos("), bg_color="black", fg_color='black').grid(row=3, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="Arctangent", command=lambda: button_click("math.atan("), bg_color="black", fg_color='black').grid(row=3, column=3, padx=5, pady=5)

# Create a button to evaluate the expression
ctk.CTkButton(root, text="Calculate", command=evaluate_expression, bg_color="black", fg_color='black').grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create a button to clear the expression and result
ctk.CTkButton(root, text="Clear", command=clear_all, bg_color="black", fg_color='black').grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# Create buttons for number input
ctk.CTkButton(root, text="1", command=lambda: button_click("1"), bg_color="black", fg_color='black').grid(row=5, column=0, padx=5, pady=5)
ctk.CTkButton(root, text="2", command=lambda: button_click("2"), bg_color="black", fg_color='black').grid(row=5, column=1, padx=5, pady=5)
ctk.CTkButton(root, text="3", command=lambda: button_click("3"), bg_color="black", fg_color='black').grid(row=5, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="4", command=lambda: button_click("4"), bg_color="black", fg_color='black').grid(row=6, column=0, padx=5, pady=5)
ctk.CTkButton(root, text="5", command=lambda: button_click("5"), bg_color="black", fg_color='black').grid(row=6, column=1, padx=5, pady=5)
ctk.CTkButton(root, text="6", command=lambda: button_click("6"), bg_color="black", fg_color='black').grid(row=6, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="7", command=lambda: button_click("7"), bg_color="black", fg_color='black').grid(row=7, column=0, padx=5, pady=5)
ctk.CTkButton(root, text="8", command=lambda: button_click("8"), bg_color="black", fg_color='black').grid(row=7, column=1, padx=5, pady=5)
ctk.CTkButton(root, text="9", command=lambda: button_click("9"), bg_color="black", fg_color='black').grid(row=7, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="0", command=lambda: button_click("0"), bg_color="black", fg_color='black').grid(row=8, column=1, padx=5, pady=5)
ctk.CTkButton(root, text=".", command=lambda: button_click("."), bg_color="black", fg_color='black').grid(row=8, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="(", command=lambda: button_click("("), bg_color="black", fg_color='black').grid(row=5, column=3, padx=5, pady=5)
ctk.CTkButton(root, text=")", command=lambda: button_click(")"), bg_color="black", fg_color='black').grid(row=6, column=3, padx=5, pady=5)  
ctk.CTkButton(root, text="pi", command=lambda: button_click("math.pi"), bg_color="black", fg_color='black').grid(row=7, column=3, padx=5, pady=5)

# Create a label to display results
result_label = ctk.CTkLabel(root, text="Result: ", width=200, bg_color="black", fg_color='black')
result_label.grid(row=9, column=0, columnspan=4, padx=5, pady=5)

# Run application
root.mainloop()
