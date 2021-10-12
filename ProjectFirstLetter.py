def count_first_letter(names):
    countOfNames = {}
    for Lname, Fname in names.items():
        if Lname[0] not in countOfNames: countOfNames[Lname[0]] = len(Fname)
        elif Lname[0] in countOfNames: countOfNames[Lname[0]] += len(Fname)
    return countOfNames

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}