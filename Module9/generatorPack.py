def create_operation(operation):
  if operation == "multiply":
    def multiply(x, y):
      return x * y

    return multiply
  elif operation == "divide":
    def divide(x, y):
      if y == 0:
        return "Error: Division by zero"
      return x / y

    return divide


multiply_func = create_operation("multiply")
print(multiply_func(3, 2))

divide_func = create_operation("divide")
print(divide_func(6, 3))
print(divide_func(6, 0))


square_lambda = lambda x: x ** 2
print(square_lambda(4))

def square_def(x):
    return x ** 2

print(square_def(4))


class Rect:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __call__(self):
    return self.a * self.b


rectangle = Rect(2, 4)
print(f"Стороны: {rectangle.a}, {rectangle.b}")
print(f"Площадь: {rectangle()}")
