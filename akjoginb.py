def p(n):
    firstNum = 1
    result = 0
    for i in range(1, n):
        firstNum += 2*i
    for j in range(n):
        result += firstNum + 2*j
    return result
    
print(p(5))