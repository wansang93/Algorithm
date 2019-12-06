from collections import Counter
mylist = list(map(str, input().split()))

def maxword(words):
	counter = Counter(words)
	max_count = -1
	for letter in counter:
		if counter[letter] > max_count:
			max_count = counter[letter]
			max_letter = letter
	return max_letter, max_count

name, num = maxword(mylist)
print("{}(이)가 총 {}표로 반장이 되었습니다.".format(name, num))