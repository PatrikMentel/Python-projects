def narcissistic(value):
    result = 0
    for digit in str(value): result += int(digit)**len(str(value))
    return True if result == value else False



def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))