def anagram(word, words):
    result = []
    for w in words:
        if sorted(list(word)) == sorted(list(w)): 
            result.append(w)
    return result

print(anagram('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))



def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]