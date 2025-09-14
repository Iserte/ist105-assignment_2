import cgi
import math

print("Assignment #2", end="\n")
print("Gustavo Iserte Bonfim - CT1010953", end="\n")

form = cgi.FieldStorage()
print(form, end="\n")

a = float(form.getvalue("a", 1))
b = float(form.getvalue("b", 1))
c = float(form.getvalue("c", 1))

print("A = ", a)
print("B = ", b)
print("C = ", c)

c_cubed = c ** 3
sqrt_cubed = c_cubed ** 0.5
division = sqrt_cubed / a
multiplied = division * 10
result = multiplied + b

print(f"<html><body><h2>Result: {result:.2f}</h2></body></html>")