def check_for_name(sentence, name):
    return True if name.lower() in sentence.lower() else False
print(check_for_name("Hello Michael", "michael"))