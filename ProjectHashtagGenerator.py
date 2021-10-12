def GenerateHashtag(text):
    if text == "" or len(text)>140: return False
    return "#" + text.title().replace(' ','')
print(GenerateHashtag(" Hello world people KATA"))