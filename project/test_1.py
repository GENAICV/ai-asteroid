# main.py

import my_module


def from_main_import():
    result1 = my_module.some_function_from_module1()
    result2 = my_module.some_function_from_module2()
    return result1,result2

# print(result1)  # Output: Hello from module1
# print(result2)  # Output: Hello from module2