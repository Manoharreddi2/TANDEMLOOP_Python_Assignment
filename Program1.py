class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower() 

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.opesration == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"


a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
op=str(input("Enter the Operation: "))
calc = Calculator(a, b, op)
print("Result:", calc.calculate())
