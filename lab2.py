import math

# Введення початкових значень
a = 2
b = 4
h = 0.2

# Функція для вибору формули в залежності від x
def f(x):
    if x <= 3:
        return math.log(x ** 3)
    elif 3 < x <= 4:
        return 1 / abs(math.sin(x))
    else:
        return 1 / math.cos(1 / x)

# Табулювання функції з кроком h
x = a
while x <= b:
    y = f(x)
    print(f"x = {x:.1f}, f(x) = {y:.2f}")
    x += h
