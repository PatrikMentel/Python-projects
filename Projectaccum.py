def accum1(s):
    result = ""
    for i, char in enumerate(s):
        result += char.upper() + char.lower()*i
        if i < len(s)-1:
            result += "-"
    return result

def accum2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
print(accum1("cwAt"))
print(accum2("cwAt"))