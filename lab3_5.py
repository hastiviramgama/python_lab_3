class Calculator:
    def __init__(self):
        self.__num1 = None
        self.__num2 = None

    def set_numbers(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def get_numbers(self):
        return self.__num1, self.__num2

    def add(self):
        return self.__num1 + self.__num2

    def subtract(self):
        return self.__num1 - self.__num2

calc = Calculator()
calc.set_numbers(10, 5)
add_result = calc.add()
subtract_result = calc.subtract()
print("Addition:", add_result)
print("Subtraction:", subtract_result)
try:
    print(calc.__num1)
except AttributeError:
    print("Error: Cannot access private variables directly.")
