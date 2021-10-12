def countOfBrackets(_string):
    leftBraces = _string.count("(")
    rightBraces = _string.count(")")
    leftBrackets = _string.count("[")
    rightBrackets = _string.count("]")
    leftCurlys = _string.count("{")
    rightCurlys = _string.count("}")
    if leftBraces == rightBraces and leftBrackets == rightBrackets and leftCurlys == rightCurlys: return True
    return False

def isValid(_string):
    _string = list(_string)
    charFound = False
    errors = 0
    bracketsBetween = 0
    testChar = ""
    if countOfBrackets(_string):
        for charStart in _string:
            if charStart == "(" or charStart == "[" or charStart == "{":
                for charEnd in _string:
                    if charStart == "(": testChar = ")"
                    if charStart == "[": testChar = "]"
                    if charStart == "{": testChar = "}"
                    if charEnd == testChar:
                        charFound = True
                        break
                    if charEnd != testChar: 
                        bracketsBetween += 1
                bracketsBetween -= 1
                if bracketsBetween % 2 != 0 or charFound == False:
                    errors += 1
                    return False
                    break
                bracketsBetween = 0
        if errors == 0: return True
    return False

x = input("Enter text: ")
print(isValid(x))