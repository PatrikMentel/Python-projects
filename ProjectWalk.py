def is_valid_walk(walk):
    return True if len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w") else False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')