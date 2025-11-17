class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation in ["add", "+"]:
            return self.a + self.b
        
        elif self.operation in ["sub", "-"]:
            return self.a - self.b
        
        elif self.operation in ["mul", "*"]:
            return self.a * self.b
        
        elif self.operation in ["div", "/"]:
            if self.b == 0:
                return "Error: Division by zero!"
            return self.a / self.b
        
        else:
            return "Invalid Operation"


a = float(input("Enter a: "))
b = float(input("Enter b: "))
operation = input("Enter operation (add/sub/mul/div or + - * /): ")

calc = Calculator(a, b, operation)
print("Result:", calc.calculate())
