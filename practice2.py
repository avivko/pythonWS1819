import random
from typing import List, Any

'''
listA = ["apple", "cheese", "seitan"]
listB = ["boy", "girl", "queer"]
listC = ["police officer", "artist", "pirate"]

story = {"food": listA, "people": listB, "jobs": listC}

print(story["food"])
'''
givenPhrase = input("please write a sentence to get it reversed and in numbers (a-e)")
crazyDict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
characterList = list(givenPhrase)
print("here is the list", characterList)
revertedList = []
revertedWithNumbers =[]
for i in characterList:
    revertedList.append(characterList[(len(characterList) - 1) - characterList.index(i)])
for i in revertedList:
    revertedWithNumbers.append(crazyDict[i])
print(''.join(revertedList))
print(''.join(str(x) for x in revertedWithNumbers))




