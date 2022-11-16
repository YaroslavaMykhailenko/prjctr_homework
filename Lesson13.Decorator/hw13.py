from __future__ import annotations
from types import FunctionType
from datetime import datetime
from msilib.schema import Error

# 1. Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations.


def check_types(function):
    def wrapper(*args, **kwargs):
        # check args
        annotations = function.__annotations__
        print(annotations)
        return_annot = annotations['return']
        annotations.pop('return')

        for element, arg_name in enumerate(annotations.keys()):
            arg_type = annotations[arg_name]
            # print('type(args[element])', type(args[element]))
            # print('arg_type', arg_type, type(arg_type))
            # print('type(args[element]) == arg_type', type(args[element]) == arg_type)
            # print('type(args[element]).__name__ ',type(args[element]).__name__)
            if type(args[element]).__name__ != arg_type:
                raise TypeError(
                    f'Argument {arg_name} must be {arg_type}, not {type(args[element]).__name__}')

        return function(*args, **kwargs)

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


print('Task 1')
# # Calculating correctly
print(add(1, 5))

# Return a print with Error
print(add(1, '5'))


# 2. Write a decorator that will calculate the execution time of a function.

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(start)
        func(*args, **kwargs)
        print(f' • Execution time: {datetime.now() - start}')
    return wrapper


@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b


print('\nTask 2')
add(1, 2)
