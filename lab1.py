# Створення змінної "city" з назвою вашого міста та її виведення
city = "Lviv"
print(city)

# Присвоєння змінній "temperature" температури в градусах Цельсія та перетворення її в градуси Фаренгейта
temperature = 15
print(temperature * 1.8 + 32)

# Присвоєння змінним значень True та False
is_sunny = True
is_raining = False

# Виведення всіх логічних операцій
print("is_sunny AND is_raining operation = ", is_sunny and is_raining)
print("is_sunny OR is_raining operation = ", is_sunny or is_raining)
print("NOT is_sunny operation = ", not is_sunny)
print("NOT is_raining operation = ", not is_raining)
print("is_sunny XOR is_raining operation = ", is_sunny != is_raining)

# Імпортування необхідних функцій з бібліотеки math
import math

# Присвоєння змінним необхідних значення
x = 3.142
z = 0.543

# Обчислення виразу та виведення результату
result = math.tan(math.sqrt(x)) + 165 * z ** 6 + (x ** 2 - z) ** (1 / 6)
print(result)