class Computer:
    def __init__(self):
        super().__init__()
        self.processor = "Intel Core I13"

    def calculate(self):
        print("I`m calculate...")

class Monitor:
    def __init__(self):
        super().__init__()
        self.diagonal = "23'"
    def display(self):
        print("I`m display info...")


class Notebook(Computer, Monitor):
    def info(self):
        print("Proc:", self.processor)
        print("Diag:", self.diagonal)


def foo(a):
    pass

notebook = Notebook()
# # notebook.calculate()
# # notebook.display()
# notebook.info()
#
#
c = Monitor()

import requests

# help(requests)

# print(Computer.__name__)
# print(foo.__name__)
# print(requests.__name__)
#
# print(type(c))
# print(type(foo))
# print(type(Computer))
# print(type(requests))
#
# for m in dir(Notebook):
#     print(m)

# c.calculate()

# if hasattr(c, "calculate"):
#     c.calculate()
#
# print(callable(foo))


print(issubclass(Monitor, Notebook))
print(issubclass(Notebook, Monitor))

