import tkinter as tk
from calculator_functions import add, subtract, multiply, divide

# Initialize the queue to store operations
queue = []

# Function to handle button clicks
def button_click(operation):
    try:
        num = float(entry.get())
        queue.append((operation, num))
        entry.delete(0, tk.END)
        result_label.config(text=f"Queued: {operation} {num}")
    except ValueError:
        result_label.config(text="Error: Invalid Input")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Function to process the queue
def process_queue():
    try:
        if not queue:
            result_label.config(text="Error: No operations queued")
            return

        result = queue[0][1]
        for operation, num in queue[1:]:
            if operation == "add":
                result = add(result, num)
            elif operation == "subtract":
                result = subtract(result, num)
            elif operation == "multiply":
                result = multiply(result, num)
            elif operation == "divide":
                result = divide(result, num)
            else:
                result_label.config(text="Error: Unknown operation")
                return
        result_label.config(text=f"Result: {result}")
        queue.clear()  # Clear the queue after processing
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Create a single entry field for numbers
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create buttons for operations
tk.Button(root, text="Add", command=lambda: button_click("add")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="Subtract", command=lambda: button_click("subtract")).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Multiply", command=lambda: button_click("multiply")).grid(row=1, column=2, padx=5, pady=5)
tk.Button(root, text="Divide", command=lambda: button_click("divide")).grid(row=1, column=3, padx=5, pady=5)

# Create buttons to process and clear the queue
tk.Button(root, text="Calculate", command=process_queue).grid(row=2, column=0, columnspan=4, padx=5, pady=5)
tk.Button(root, text="Clear", command=lambda: entry.delete(0, tk.END)).grid(row=2, column=2, columnspan=4, padx=5, pady=5)

# Create buttons for numbers
tk.Button(root, text="1", command=lambda: entry.insert(tk.END, "1")).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="2", command=lambda: entry.insert(tk.END, "2")).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="3", command=lambda: entry.insert(tk.END, "3")).grid(row=3, column=2, padx=5, pady=5)
tk.Button(root, text="4", command=lambda: entry.insert(tk.END, "4")).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="5", command=lambda: entry.insert(tk.END, "5")).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="6", command=lambda: entry.insert(tk.END, "6")).grid(row=4, column=2, padx=5, pady=5)
tk.Button(root, text="7", command=lambda: entry.insert(tk.END, "7")).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="8", command=lambda: entry.insert(tk.END, "8")).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="9", command=lambda: entry.insert(tk.END, "9")).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="0", command=lambda: entry.insert(tk.END, "0")).grid(row=6, column=1, padx=5, pady=5)

# Create a label to display results
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

# Run application
root.mainloop()
