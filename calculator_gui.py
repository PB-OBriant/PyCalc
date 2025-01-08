import tkinter as tk
from calculator_functions import add, subtract, multiply, divide

# Function to handle button clicks
def button_click(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = add(num1, num2)

        elif operation == "subtract":
            result = subtract(num1, num2)

        elif operation == "multiply":
            result = multiply(num1, num2)

        elif operation == "divide":
            result = divide(num1, num2)

        else:
            result = "Error...unknown operation"
        
        # Update result label with the calculated result
        result_label.config(text=f"Result: {result}")

    # catch errors that the user may input to break the program
    except ValueError:
        result_label.config(text="Error: Invalid Input")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create application window
root = tk.Tk()
root.title("Calculator")  # Name the window
root.geometry("300x400")  # Set the window size

# Create entry fields for numbers
tk.Label(root, text="Entry1:").grid(row=0, column=1, padx=5, pady=5)
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Entry2:").grid(row=0, column=3, padx=5, pady=5)
entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=4, padx=5, pady=5)

# Create buttons for operations
tk.Button(root, text="Add", command=lambda: button_click("add")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="Subtract", command=lambda: button_click("subtract")).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Multiply", command=lambda: button_click("multiply")).grid(row=1, column=2, padx=5, pady=5)
tk.Button(root, text="Divide", command=lambda: button_click("divide")).grid(row=1, column=3, padx=5, pady=5)

# Create a label to display results
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# Run application
root.mainloop()
