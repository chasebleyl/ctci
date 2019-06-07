# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hints: #44, #117, #132

import unittest

###
## Second attempt, referring to Solution
# O(N)

def unique_string(string):
	# ASCII character set is only 128 characters large
	if len(string) > 128:
		return False
	char_set = [ False ] * 128
	for char in string:
		index_char = ord(char)
		if char_set[index_char]:
			return False
		char_set[index_char] = True
	return True

###
## First attempt:
# O(N^2)
#
# def unique_string(string):
# 	for i in range(0, len(string)):
# 		base_char = string[i]
# 		for j in range(i + 1, len(string)):
# 			if base_char == string[j]:
# 				return False
# 	return True

class Test(unittest.TestCase):
	'''Test Cases'''
	data = [
		['abc', True],
		['ABC', True],
		['abA', True],
		['abAB', True],
		['123', True],
		['1a2b', True],
		['abcdefg', True],
		['aba', False],
		['ABA', False],
		['abab', False],
		['1212', False],
		['abcdefga', False]
	]
	
	def test_unique_strings(self):
		for [string, expected] in self.data:
			result = unique_string(string)
			self.assertEqual(result, expected)

if __name__ == "__main__":
	unittest.main()	
