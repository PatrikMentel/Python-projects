def substring(word, start, end):
    if start in word and end in word:
        return word[word.index(start)+1:word.index(end)]
    return word
print(substring("apple", "p", "e"))