import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        choice = operator_entry.get()

        if choice == "+":
            result = f"{num1} + {num2} = {num1 + num2}"
        elif choice == "-":
            result = f"{num1} - {num2} = {num1 - num2}"
        elif choice == "x":
            result = f"{num1} x {num2} = {num1 * num2}"
        elif choice == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = f"{num1} / {num2} = {num1 / num2}"
        else:
            result = "Invalid. Please enter the correct operator"

        result_label.config(text=result)

    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("500x350")

tk.Label(root, text="Welcome to the Basic Calculator", font=("Arial", 12, "bold")).pack(pady=5)

tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter the operator (+, -, x, /)").pack()
operator_entry = tk.Entry(root)
operator_entry.pack()


tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack()

root.mainloop()


