def values_that_are_keys(my_dictionary):
    listFromDictionary = []
    for key, value in my_dictionary.items():
        if value in my_dictionary:
            listFromDictionary.append(value)
    return listFromDictionary

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]