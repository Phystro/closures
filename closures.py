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
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = open('output_path', 'w')

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
