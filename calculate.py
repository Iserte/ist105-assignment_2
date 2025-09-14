import cgi
import math

print("Content-type: text/html\n")

form = cgi.FieldStorage()
a = float(form.getvalue("a", 1))
b = float(form.getvalue("b", 1))
c = float(form.getvalue("c", 1))

c_cubed = c ** 3
sqrt_cubed = c_cubed ** 0.5
division = sqrt_cubed / a
multiplied = division * 10
result = multiplied + b

print(f"<html><body><h2>Result: {result:.2f}</h2></body></html>")