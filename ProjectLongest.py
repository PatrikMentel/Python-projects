def longest1(a, b):
    sortedList = []
    for char in a:
        if char not in sortedList:
            sortedList.append(char)
    for char in b:
        if char not in sortedList:
            sortedList.append(char)
    sortedList.sort()
    return "".join(sortedList)

def longest2(s1, s2):
    return ''.join(sorted((set(s1+s2))))

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest1(a, b))
print(longest2(a, b))