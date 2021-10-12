def make_spoonerism(word1, word2):
    return word2[0]+word1[1:]+" "+word1[0]+word2[1:]
print(make_spoonerism("Codecademy", "Learn"))