anagrams={}
words=['cat','pat','bat','tab']
for word in words:
    sortedword=''.join(sorted(word))
    print(sortedword)
    if sortedword in anagrams:
        anagrams[sortedword].append(word)
    else:
        anagrams[sortedword]=[word]
print(anagrams)
print(len(anagrams))

# act
# apt
# abt
# abt
# {'act': ['cat'], 'apt': ['pat'], 'abt': ['bat', 'tab']}
# 3

