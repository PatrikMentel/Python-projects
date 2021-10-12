def digital_root(n):
    n = str(n)
    result = 0
    while len(n) > 1:
        result = 0
        for digit in n:
            result += eval(digit)
            n = str(result)
    return result
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))