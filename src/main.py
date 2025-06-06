def bad_character_table(needle):
    table = {}
    for i in range(len(needle) - 1):
        table[needle[i]] = len(needle) - i - 1
    return table

def boyer_moore_search(haystack, needle):
    if not needle or not haystack:
        return []

    positions = []
    shift_table = bad_character_table(needle)
    i = 0

    while i <= len(haystack) - len(needle):
        skip = 0
        for j in reversed(range(len(needle))):
            if needle[j] != haystack[i + j]:
                skip = shift_table.get(haystack[i + j], len(needle))
                break
        if skip == 0:
            positions.append(i)
            i += 1
        else:
            i += skip
    return positions

def extract_todos_from_file(file_path):
    todos = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "# todo" in line.lower():
                todos.append(line.strip())
    return todos
  
if __name__ == "__main__":
    file = "fake_code_file.py"
    todos = extract_todos_from_file(file)
    print("== TODO коментарі у файлі ==\n")
    for todo in todos:
        print(todo)
