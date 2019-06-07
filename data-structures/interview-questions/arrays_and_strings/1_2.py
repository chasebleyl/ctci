# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Hints: #1, #84, #122, #131

from collections import Counter
import unittest

###
# Second Attempt (with help from solution): No external packages required
# O(N)
def check_permutation(string_one, string_two):
	if len(string_one) != len(string_two):
		return False
	counter = [ 0 ] * 128 # ASCII assumption
	for char in string_one:
		counter[ord(char)] += 1
	for char in string_two:
		if counter[ord(char)] == 0:
			return False
		counter[ord(char)] -= 1
	return True 
	
# ###
# # First Attempt (with help from https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/2_Check%20Permutation/CheckPermutation.py)
# # O(N)
# def check_permutation(string_one, string_two):
# 	if len(string_one) != len(string_two):
# 		return False
# 	counter = Counter()
# 	for char in string_one:
# 		counter[char] += 1
# 	for char in string_two:
# 		if counter[char] == 0:
# 			return False
# 		counter[char] -= 1
# 	return True    

# ###
# # Third Attempt (with help from solution): sort strings then compare, less efficient than first & third but very clear
# # O(N log N)
# def check_permutation(string_one, string_two):
# 	if len(string_one) != len(string_two):
# 		return False
# 	sorted_one = ''.join(sorted(string_one))
# 	sorted_two = ''.join(sorted(string_two))
# 	if sorted_one != sorted_two:
# 		return False
# 	return True

class Test(unittest.TestCase):
	'''Test Cases'''
	data = [
		['abc', 'bac', True],
		['bbb', 'bbb', True],
		['12345', '54321', True],
		['abc', 'ab', False],
		['cde', 'bcd', False],
		['12345', 'abcde', False]
	]
	
	def test_permutations(self):
		for [string_one, string_two, expected] in self.data:
			result = check_permutation(string_one, string_two)
			self.assertEqual(result, expected)

if __name__ == "__main__":
	unittest.main()	
