def replaceLast(string, replacedCharacter, replacement):
    commas = 0
    for char in string:
        if char == replacedCharacter.strip(): commas += 1
    string = string.replace(replacedCharacter, replacement, commas)
    string = string.replace(replacement, replacedCharacter, commas-1)
    return string
    
def addToResult(type, value, remainder, result):
    if value > 0: result += str(value) + type
    if value > 1: result += "s"
    if remainder != 0 and value > 0 and type != " second": result += ", "
    return result

def format_duration(s):
    if s > 0:
        result = ""

        #YEARS
        years = s // 31536000
        remainder = s % 31536000
        result = addToResult(" year", years, remainder, result)

        #DAYS
        days = remainder // 86400
        remainder = remainder % 86400
        result = addToResult(" day", days, remainder, result)

        #HOURS
        hours = remainder // 3600
        remainder = remainder % 3600
        result = addToResult(" hour", hours, remainder, result)

        #MINUTES
        minutes = remainder // 60
        remainder = remainder % 60
        result = addToResult(" minute", minutes, remainder, result)

        #SECONDS
        seconds = remainder
        result = addToResult(" second", seconds, remainder, result)

        result = replaceLast(result, ", ", " and ")
        return result
    return 0
seconds = input("Enter number of seconds: ")
print(format_duration(int(seconds)))








#Not mine but learned something new :D
def replace_last(_string, delimiter, replacement):
    start, _, end = _string.rpartition(delimiter)
    return start + replacement + end