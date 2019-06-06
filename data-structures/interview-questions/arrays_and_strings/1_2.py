# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Hints: #1, #84, #122, #131

from collections import Counter

valid_permutations = [ ['abc', 'bac'], ['bbb', 'bbb'], ['12345', '54321'] ]
invalid_permutations = [ ['abc', 'ab'], ['cde', 'bcd'], ['12345', 'abcde'] ]

def validate_permutations(permutations, expected_result):
	for permutation in permutations:
		result = check_permutation(permutation[0], permutation[1])
		if result != expected_result:
			print("For strings " + str(permutation[0]) + " and " + str(permutation[1])  + " expected " + str(expected_result) + " but got " + str(result))

###
# First Attempt (with help from https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/2_Check%20Permutation/CheckPermutation.py)
# O(N)

def check_permutation(string_one, string_two):
	if len(string_one) != len(string_two):
		return False
	counter = Counter()
	for char in string_one:
		counter[char] += 1
	for char in string_two:
		if counter[char] == 0:
			return False
		counter[char] -= 1
	return True    
	
validate_permutations(valid_permutations, True)
validate_permutations(invalid_permutations, False)

print("Finished validating permutations!")
	