def max_key(my_dictionary):
    maximum = max(my_dictionary.values())
    for key in my_dictionary:
        if my_dictionary[key] == maximum: return key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"