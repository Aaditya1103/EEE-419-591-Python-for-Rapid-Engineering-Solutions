##################################################
#          Name:- Aaditya Sakhardande            #
#          ASU ID:- 1233720594                   #
#          Email:- asakhar3@asu.edu              #
#          Date:- 02/20/2025                     #
##################################################
import tkinter as tk
import math
import re

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartCalc")
        self.root.geometry("390x500")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.expression = tk.StringVar()
        entry = tk.Entry(self.root, textvariable=self.expression, font=("Arial", 18), bd=8, relief=tk.RIDGE, justify="right")
        entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, pady=10)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
            ["**", "log", "sin", "cos"]
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                tk.Button(self.root, text=char, font=("Arial", 14), width=7, height=2,
                          command=lambda ch=char: self.process_input(ch)).grid(row=r + 1, column=c, padx=5, pady=5)

    def process_input(self, char):
        current_text = self.expression.get()

        if char == "=":
            try:
                modified_text = self.convert_expression(current_text)
                result = eval(modified_text, {"math": math})
                self.expression.set(str(result))
            except Exception:
                self.expression.set("Error")

        elif char == "C":
            self.expression.set("")

        elif char in ["log", "sin", "cos"]:
            try:
                last_number = self.extract_last_number(current_text)
                if last_number is not None:
                    if char == "log":
                        result = math.log(float(last_number))
                    elif char == "sin":
                        result = math.sin(math.radians(float(last_number)))
                    elif char == "cos":
                        result = math.cos(math.radians(float(last_number)))

                    new_text = current_text[: -len(last_number)] + str(result)
                    self.expression.set(new_text)
                else:
                    self.expression.set("Error")
            except Exception:
                self.expression.set("Error")

        else:
            self.expression.set(current_text + char)

    def extract_last_number(self, text):
        """Extracts the last valid number from the expression."""
        match = re.search(r"(\d+(\.\d+)?)$", text)
        return match.group(1) if match else None

    def convert_expression(self, expr):
        """Converts sin, cos, and log functions into valid math expressions for eval()."""
        expr = re.sub(r"sin\(([^)]+)\)", r"math.sin(math.radians(\1))", expr)
        expr = re.sub(r"cos\(([^)]+)\)", r"math.cos(math.radians(\1))", expr)
        expr = re.sub(r"log\(([^)]+)\)", r"math.log(\1)", expr)
        return expr

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
