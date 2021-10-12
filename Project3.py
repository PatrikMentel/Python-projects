"""num = input("Enter number: ")
partsOfNum = list(str(num))
line = ""
i = len(partsOfNum)-1
for part in partsOfNum:
    if part != "0":
        line += " + "
    if part != "0":
        line += part + "0"*i
    i -= 1
print(line)"""