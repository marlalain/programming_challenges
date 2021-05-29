#!/bin/python3
# Project Euler - Problem 001

x = 0
for i in range(0, 1000):
    if (i % 3) == 0 or (i % 5) == 0:
        x = x + i
print("Result: ", x)
