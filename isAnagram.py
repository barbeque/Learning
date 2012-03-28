def isAnagram(bigWord, smallWord):
	sortedBigWord = sorted(list(str.lower(bigWord)))
	sortedSmallWord = sorted(list(str.lower(smallWord)))

	if len(sortedSmallWord) > len(sortedBigWord):
		return False

	bigWordStart = 0
	for i in range(0, len(sortedSmallWord)):
		for j in range(bigWordStart, len(sortedBigWord)):
			if ord(sortedBigWord[j]) > ord(sortedSmallWord[i]):
				return False
			elif ord(sortedBigWord[j]) == ord(sortedSmallWord[i]):
				bigWordStart = j + 1 # prevents doubles
				break
	return True

assert isAnagram("airplane", "plane") is True, "plane is not inside airplane?"
assert isAnagram("helicopter", "chop") is True, "chop is not inside helicopter?"
assert isAnagram("nipples", "pip") is True, "double letters don't work?"
assert isAnagram("cheese", "kuwait") is False, "kuwait is not an anagram of cheese"
assert isAnagram("geoff", "fog") is True, "kuwait is not an anagram of cheese"
