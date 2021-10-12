def length(sentence, x):
    sentence = sentence.split(" ")
    for word in sentence:
        if len(word) < x: return False
    return True
print(length("I like apples", 2))
print(length("He likes apples", 2))