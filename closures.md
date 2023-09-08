
Implement a function clalled `compose` that takes an arbitrary number of functions as its arguments.

It should return a new function that represents the composition of functionsList[1], functionsList[2], functionsList[3],...,functionsList[n] such that the arguments given to the function returned by the compose are passed to functionsList[1], the output obtained is passed to functionsList[2], and so on. Finally, the output of the last function should be returned.

Note: the function `compose` should return a function. Each function may receive a single argument or a list of arguments.

The functions used are:
add(*args) -> takes a variable number of arguments and returns the sum of the arguments

square(a) -> takes number or list of numbers as an argument and returns square of each element in a.

splitter(a) -> takes a number as an argument, divides the number by 2 and returns a list of length 2: [floor of division, value - floor of division]. If a is a list, splitter() concatenates the output of the other lists.

my_max(a) -> takes a number or list of numbers as an argument and returns the maximum value.

my_min(a) -> takes number or list of numbers as an argument and returns minimum value

The initial code is as below:

```py
#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Callable
    
def add(*args):
    result = 0
    for x in args:
        result += x
    return result


def square(a):
    if isinstance(a, (list, tuple)):
        return [b * b for b in a]
    return a * a


def splitter(a):
    if isinstance(a, (list, tuple)):
        return sum([splitter(b) for b in a], [])
    return [a // 2, (a + 1) // 2]


def my_max(a):
    if isinstance(a, (list, tuple)):
        return max(a)
    return a


def my_min(a):
    if isinstance(a, (list, tuple)):
        return min(a)
    return a

#
# Complete the 'compose' function below.
#
# The function is expected to return a FUNCTION.
# The function accepts following parameters:
#  1. ARGUMENTS *functionsList
#

def compose(*functionsList: Callable) -> Callable:
    # Write your code here

    def cfunction(*args):
        result = args
        # for func in functionsList:
            
        for func in functionsList:
            print('Function -> ', func.__name__)
            if isinstance(result, list) and not isinstance(result, int):
                if len(result) == 1:
                    print(type(result), " len(result) == 1 type for ", result)
                    result = [func(result[0])]
                else:
                    print(type(result), " len(result) != 1 type for ", result)
                    result = [func(*result)]
            else:
                print(type(result), " type for ", result, ' of length: ', len(result))
                result = [func(*result)]
        return result[0] if len(result) == 1 else result

    return cfunction

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    functionMapper = {
        "add": add,
        "square": square,
        "splitter": splitter,
        "my_max": my_max,
        "my_min": my_min,
    }

    functionsList_count = int(input().strip())

    functionsList = []

    for _ in range(functionsList_count):
        functionsList_item = input()
        functionsList.append(functionMapper[functionsList_item])

    composedFunctions = compose(*functionsList)

    argumentsList_count = int(input().strip())

    argumentsList = []

    for _ in range(argumentsList_count):
        argumentsList_item = int(input().strip())
        argumentsList.append(argumentsList_item)

    result = composedFunctions(*argumentsList)

    fptr.write(str(result) + "\n")

    fptr.close()

```

## Explanation
The `compose` function takes an arbitrary number of functions as arguments, and returns a new function `cfunction` that represents the composition of those functions.

Inside `cfunction`, it iterates through the functions in `functionsList` adn applies each function to the result of the previous one, effectively chaining the functions together.
