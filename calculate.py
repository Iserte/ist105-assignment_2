import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

c_cubed = c ** 3
sqrt_cubed = c_cubed ** 0.5
division = sqrt_cubed / a
multiplied = division * 10
result = multiplied + b

print("Content-type: text/html\n")
print(f"""
<html>
  <head><title>Assignment #2</title></head>
  <body>
    <h1>Assignment #2</h1>
    <p><strong>Gustavo Iserte Bonfim - CT1010953</strong></p>
    <p>A = {a}</p>
    <p>B = {b}</p>
    <p>C = {c}</p>
    <h2>Result: {result:.2f}</h2>
  </body>
</html>
""")
