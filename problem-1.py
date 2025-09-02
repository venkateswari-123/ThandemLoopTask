#python programmin language
class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()  # make case-insensitive

    def calculate(self):
        if self.operation == "add" or self.operation == "addition":
            return self.a + self.b
        elif self.operation == "sub" or self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "mul" or self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "div" or self.operation == "division":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Invalid operation"
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add, sub, mul, div): ")

calc = Calculator(a, b, operation)
result = calc.calculate()
print("Result:", result)
