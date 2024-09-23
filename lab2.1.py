# Введення початкових значень
a = 0.1
b = 0.6
h = 0.05
d = 0.001

# Табулювання функції (сума ряду)
def function(x, d):
    sum = 0
    k = 1
    first_in_line = k * x ** k
    while abs(first_in_line) > d:
        sum += first_in_line
        k += 1
        first_in_line = k * x ** k
    return sum

# Табулювання з кроком h
x = a
while x <= b:
    y = function(x, d)
    print(f"x = {x:.2f}, S(x) = {y:.5f}")
    x += h
