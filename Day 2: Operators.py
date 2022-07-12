#!/bin/python3

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    gorjeta = tip_percent / 100
    taxa = tax_percent / 100
    total = (meal_cost * gorjeta) + (meal_cost * taxa) + meal_cost
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
