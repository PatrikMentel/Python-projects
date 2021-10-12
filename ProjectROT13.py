def ROT13(text):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in text:
        if char in alphabet:
            if alphabet.index(char)+13 < len(alphabet):
                result += alphabet[alphabet.index(char)+13]
            else: result += alphabet[alphabet.index(char)+13-len(alphabet)]
        else: result += char
    return result

print(ROT13("Hello123zZ!"))