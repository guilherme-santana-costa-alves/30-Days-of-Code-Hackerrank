#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    #using the print funcion with the * to unpack iterables into a list/tuple and then i used [::-1] to reverse order
    print(*arr[::-1])
