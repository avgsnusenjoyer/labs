def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        L = int(lines[0])
        pyramid = [list(map(int, line.strip().split())) for line in lines[1:]]
    return L, pyramid

def solve_career(L, pyramid):
    # Копія останнього рівня — значення досвіду
    result = pyramid[-1][:]
    
    # Для відновлення шляху: зберігаємо "куди йти далі"
    path_indices = [[-1] * len(row) for row in pyramid]
    
    for level in range(L - 2, -1, -1):
        new_result = []
        for i in range(len(pyramid[level])):
            left = result[i]
            right = result[i + 1]
            
            # Вибираємо більший досвід і запам’ятовуємо напрямок
            if left > right:
                max_experience = pyramid[level][i] + left
                path_indices[level][i] = i      # йдемо вниз зліва
            else:
                max_experience = pyramid[level][i] + right
                path_indices[level][i] = i + 1  # йдемо вниз справа

            new_result.append(max_experience)
        result = new_result

    # Відновлення шляху
    path = []
    index = 0
    for level in range(L):
        path.append(pyramid[level][index])
        if level < L - 1:
            index = path_indices[level][index]

    return result[0], path

def write_output(filename, result, path):
    with open(filename, 'w') as f:
        f.write("Максимальний досвід: " + str(result) + '\n')
        f.write("Шлях: " + ' '.join(map(str, path)) + '\n')

if __name__ == "__main__":
    L, pyramid = read_input("career.in")
    result, path = solve_career(L, pyramid)
    write_output("career.out", result, path)
