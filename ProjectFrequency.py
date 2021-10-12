def frequency_dictionary(words):
    my_dictionary = {}
    for word in words:
        my_dictionary.update({word: words.count(word)})
    return my_dictionary

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}