"""
Create an instance of a simple calculator.

Classes:

    Calculator
"""

from numbers import Number

class Calculator:
    """
    A calculator with 5 arithmetic functions: addition, subtraction, multiplication,
    division, taking root of a number.
    The calculator instance has its own memory which can be reset.

    Methods
    -------
    add(number: float):
        adds a number to the memory of the calculator
    subtract(number: float):
        subtracts a number from the memory of the calculator
    multiply(number: float):
        multiplies the memory of the calculator by a number
    divide(divisor: float):
        divides the memory of the calculator by the divisor
    take_root(root_degree: int):
        take a root_degree root of the memory of the calculator
    reset_memory():
        reset the memory of the calculator to 0
    """
    def __init__(self, memory: float = 0.) -> None:
        """
        Constructs the memory attribute for the calculator instance
        """
        if self.check_type_not_complex(number=memory):
            self.__memory = memory

    def add(self, number: float) -> float:
        """
        Adds a number to the memory of a calculator
        """
        if self.check_type_not_complex(number=number):
            self.__memory += number
            return self.__memory
        return self.__memory

    def subtract(self, number: float) -> float:
        """
        Subtracts a number from the memory of a calculator
        """
        if self.check_type_not_complex(number=number):
            self.__memory -= number
            return self.__memory
        return self.__memory

    def multiply(self, number: float) -> float:
        """
        Multiplies the number in the memory of a calculator
        """
        if self.check_type_not_complex(number=number):
            self.__memory *= number
            return self.__memory
        return self.__memory

    def divide(self, divisor: float) -> float:
        """
        Divides the number in the memory of a calculator
        """
        if self.check_type_not_complex(number=divisor):
            try:
                self.__memory /= divisor
                return self.__memory
            except ZeroDivisionError:
                print("Division by zero is not allowed")
                return self.__memory
        return self.__memory

    def take_root(self, root_degree: int) -> float:
        """
        Takes a root_degree root of the number in the memory of a calculator
        """
        if isinstance(root_degree, int):
            try:
                exponent = 1 / root_degree
                root_result = self.__memory ** exponent
                if self.check_type_not_complex(root_result):
                    self.__memory = root_result
                    return self.__memory
                if self.__memory < 0:
                    print("Taking root of a negative number results in a complex number")
                    return self.__memory
            except ZeroDivisionError:
                print("Taking the zeroth root is not allowed")
                return self.__memory
        print("Root degree must be integer")
        return self.__memory

    def display_memory(self) -> None:
        """
        Displays the currently stored number in the memory of the calculator
        """
        return self.__memory

    def reset_memory(self) -> None:
        """
        Resets the memory of the calculator to 0
        """
        self.__memory = 0
        return self.__memory

    @classmethod
    def check_type_not_complex(cls, number: Number) -> None:
        """
        Helper function to determine if the number is not complex number
        """
        if isinstance(number, complex):
            print("Calculator supports arithmetic only with integers",
                    "and floats but not with complex numbers")
            return False
        return True
