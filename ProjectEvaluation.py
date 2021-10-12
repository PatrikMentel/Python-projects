def evaluate(num, args):
    try:
        return eval(num + args)
    except ZeroDivisionError:
        return "Can't divide by zero!"
def zero(args = None): 
    if args != None: return evaluate("0", args)
    if args == None: return 0
def one(args = None):  
    if args != None: return evaluate("1", args)
    if args == None: return 1
def two(args = None): 
    if args != None: return evaluate("2", args)
    if args == None: return 2
def three(args = None): 
    if args != None: return evaluate("3", args)
    if args == None: return 3
def four(args = None): 
    if args != None: return evaluate("4", args)
    if args == None: return 4
def five(args = None): 
    if args != None: return evaluate("5", args)
    if args == None: return 5
def six(args = None): 
    if args != None: return evaluate("6", args)
    if args == None: return 6
def seven(args = None): 
    if args != None: return evaluate("7", args)
    if args == None: return 7
def eight(args = None): 
    if args != None: return evaluate("8", args)
    if args == None: return 8
def nine(args = None): 
    if args != None: return evaluate("9", args)
    if args == None: return 9

def plus(args): 
    return " + " + str(args)
def minus(args): 
    return " - " + str(args)
def times(args): 
    return " * " + str(args)
def divided_by(args): 
    return " // " + str(args)

result = one(plus(eight()))
print(result)