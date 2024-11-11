def to_lowercase(letter):
    if 'A' <= letter <= 'Z':
        return chr(ord(letter) + 32)
    return letter

def is_isogram(word):
    seen_letters = []

    for letter in word:
        lower_letter = to_lowercase(letter)
        if lower_letter in seen_letters:
            return False
        seen_letters.append(lower_letter)

    return True

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
