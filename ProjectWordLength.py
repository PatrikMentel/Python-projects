def word_length_dictionary(words):
    my_dictionary = {}
    for word in words:
        my_dictionary[word] = len(word)
    return my_dictionary

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}