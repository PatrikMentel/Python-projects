def unique_values(my_dictionary):
    unique = set()
    for value in my_dictionary.values():
        unique.add(value)
    return len(unique)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1