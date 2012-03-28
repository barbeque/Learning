# checks if 'smallWord' is an anagram of 'bigWord'
def isAnagram(bigWord, smallWord):
	sortedBigWord = sorted(list(str.lower(bigWord)))
	sortedSmallWord = sorted(list(str.lower(smallWord)))

	if len(sortedSmallWord) > len(sortedBigWord):
		return False

	bigWordStart = 0
	for i in range(0, len(sortedSmallWord)):
		for j in range(bigWordStart, len(sortedBigWord)):
			if sortedBigWord[j] > sortedSmallWord[i]:
				return False
			elif sortedBigWord[j] == sortedSmallWord[i]:
				bigWordStart = j + 1 # prevents doubles
				break
	return True

assert isAnagram("airplane", "plane") is True, "plane is an anagram of airplane"
assert isAnagram("helicopter", "chop") is True, "chop is an anagram of helicopter"
assert isAnagram("nipples", "pip") is True, "double letters don't work?"
assert isAnagram("cheese", "kuwait") is False, "kuwait is not an anagram of cheese"
assert isAnagram("Geoff", "fog") is True, "fog is an anagram of Geoff"
assert isAnagram("small", "smallsmall") is False, "anagrams can't be longer than the words they are anagrams of!"
assert isAnagram("djibouti", "about") is False, "clever seeming false anagrams will still fail!"
assert isAnagram("barbeque", "barber") is False, "can't double up illegally!"
assert isAnagram("Anaheim", "Hemi") is True, "mixed case works for both!"