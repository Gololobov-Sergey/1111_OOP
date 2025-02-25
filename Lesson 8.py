import datetime


class MyException(Exception):
    def __init__(self, date, line, message):
        self.__date = date
        self.__line = line
        self.__message = message

    def save(self, fname):
        f = open(fname, 'a', encoding='utf-8')
        f.write(str(self.__date) + ', Line' + self.__line + ", Message:" + self.__message + "\n")
        f.close()


#
# try:
#     a = int(input())
#     print(a)
#     if a == 0:
#         # raise MyException(datetime.datetime.now(), "18", "Спроба ділення на 0!!!")
#         raise ZeroDivisionError("qwdqwedqw")
#     print(1/a)
#     print(aaa)
# except (NameError, ValueError) as err:
#     print(err)
#     print("Name or Value Error")
# except ZeroDivisionError as err:
#     print("Zero Division Error")
#     print(err)
# except MyException as err:
#     err.save("log.txt")
# except:
#     print("Fatal Error")
#
#
# print("Code...")


def check_value(var1):
    if type(var1) != str:
        raise TypeError("var1 not string!")
    else:
        return var1



# try:
#     a = []
#     a = check_value(a)
#     print(a)
# except TypeError as e:
#     print(e)


result = []
def divider(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if b != 0:
            return a/b
        else:
            raise ZeroDivisionError
    else:
        raise ValueError

data = {10: 2, 2: 5, "123": 4, 18: 0, 15:[], 8 : 4} #"123": 4, 18: 0, []: 15, 8 : 4

for key in data.keys():
    try:
        res = divider(key, data[key])
        result.append(res)
    except:
        print("Error data")

print(result)

