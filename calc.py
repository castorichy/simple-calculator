import os
from posix import system

class Calculator:
    """Simple Calculator that calculates mixture of operations in one line
    Examole: 2 + 4 * 3 / 2 = 8"""
    __op = [ "/", "*", "+", "-" ]
    __test = []
    __res = 0.0
    def __init__(self) -> None:
        """Initializes the Atributes"""
        self.__op = Calculator.__op
        self.__test = Calculator.__test
        self.__res = Calculator.__res
        #self.__test = string.split(" ")

    def calculate(self, string=[]) -> float:
        """Doese All the calculations necessary and return the results"""
        self.__test = string
        for e in self.__op:
        # loops through op (operators)
            for j, f in enumerate(self.__test):
            # loops through test (values to work on -- test)
                if e == f:
                    print(e, f)
                    match f:
                        case "/":
                            self.__res = float(self.__test[j - 1]) / float(self.__test[j + 1])
                            self.__removes(j)
                        case "*":
                            self.__res = float(self.__test[j - 1]) * float(self.__test[j + 1])
                            self.__removes(j)
                        case "+":
                            self.__res = float(self.__test[j - 1]) + float(self.__test[j + 1])
                            self.__removes(j)
                        case "-":
                            self.__res = float(self.__test[j - 1]) - float(self.__test[j + 1])
                            self.__removes(j)
        return self.__res


    def __removes(self, j):
        """Deletes value used in test list and inserts final results"""
        self.__test.pop(j + 1)
        self.__test.pop(j)
        self.__test.pop(j - 1)
        self.__test.insert(j - 1, str(self.__res))


''' def createObject():
    """Creating an object for Calculator class"""
    os.system('cls' if os.name == 'nt' else 'clear')
    strg = input("""\
\tJust a simple Calculator
Opertors to be used:
    add = +
    subtract = -
    multiplication = *
    Devision = /
    Reminder = % not implimented
Example:
1 + 2 - 3 * 4 / 3
Also remember to seperate number and operator with one space in betwee
\tEnter math operatoion
>>> """)'''
if __name__ == "__main__":
    createObject()
