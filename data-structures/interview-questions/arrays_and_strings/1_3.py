# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 
# O(N)

import unittest

def urlify(string, length):
	char_array = [None] * length
	active_space = True # Make sure we start with a character, not a space
	i = 0
	for char in string:
		if i == length:
			break
		if char != ' ':
			char_array[i] = char
			i += 1
			active_space = False
		elif active_space is False:
			char_array[i] = '%20'
			i += 1
			active_space = True
	return ''.join(char_array)

class Test(unittest.TestCase):
	'''Test Cases'''
	data = [
		('Mr John Smith     ', 13,'Mr%20John%20Smith'),
		('Moe  is   tired', 12, 'Moe%20is%20tired'),
		("   Leading spaces don't count", 26, "Leading%20spaces%20don't%20count"),
	]
	
	def test_urlify(self):
		for [test_string, length, expected] in self.data:
			actual = urlify(test_string, length)
			self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()
