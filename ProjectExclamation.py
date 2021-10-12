def add_exclamation(word):
    word += "!"*(20-len(word))
    return word
print(add_exclamation("Codecademy"))