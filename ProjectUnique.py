def unique(word):
    word = list(set(word))
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in word:
        if char in alphabet: count += 1
    return count

print(unique("Hello henry"))