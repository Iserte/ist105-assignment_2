import sys
import math

print("Assignment #2", end="\n")
print("Gustavo Iserte Bonfim - CT1010953", end="\n")

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

print("A = ", a)
print("B = ", b)
print("C = ", c)

c_cubed = c ** 3
sqrt_cubed = c_cubed ** 0.5
division = sqrt_cubed / a
multiplied = division * 10
result = multiplied + b

print(f"<html><body><h2>Result: {result:.2f}</h2></body></html>")