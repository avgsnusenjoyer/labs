def bubble_sort_row(matrix):
    """Сортує рядки матриці за зростанням методом обміну."""
    for row in matrix:
        n = len(row)
        for i in range(n):
            for j in range(0, n - i - 1):
                if row[j] > row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
    return matrix

def find_min_in_columns(matrix):
    """Знаходить мінімальний елемент у кожному стовпці."""
    num_columns = len(matrix[0])
    return [min(row[i] for row in matrix) for i in range(num_columns)]

def product_of_elements(elements):
    """Обчислює добуток елементів."""
    result = 1
    for element in elements:
        result *= element
    return result

matrix = [
    [34, -8, 27, 7, 12],
    [-5, -23, 45, 67, -2],
    [13, -12, 34, -3, 25],
    [17, 56, -6, 17, 21],
    [0, 15, 4, 9, -14]
]

sorted_matrix = bubble_sort_row(matrix)

min_in_columns = find_min_in_columns(sorted_matrix)

product_of_min_elements = product_of_elements(min_in_columns)

print("Відсортована матриця:")
for row in sorted_matrix:
    print(row)

print("\nМінімальні елементи у кожному стовпці:", min_in_columns)
print("Добуток мінімальних елементів:", product_of_min_elements)
