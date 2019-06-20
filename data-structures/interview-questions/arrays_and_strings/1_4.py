# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# O(N)

import unittest

def is_palindrome_permutation(test_string):
  table = [0 for _ in range(ord('z') - ord('a') + 1)]
  countodd = 0
  for char in test_string:
    x = char_number(char)
    if x != -1:
      table[x] += 1
      if table[x] % 2:
        countodd += 1
      else:
        countodd -= 1
  return countodd <= 1

def char_number(char):
  a = ord('a')
  z = ord('z')
  A = ord('A')
  Z = ord('Z')
  char_val = ord(char)
  
  if a <= char_val <= z:
    return char_val - a
  elif A <= char_val <= Z:
    return char_val - A
  return -1

class Test(unittest.TestCase):
	'''Test Cases'''
	data = [
		('Tact Coa', True),
		('Care arc', True),
		('ABCDEFG', False),
	]
	
	def test_palindrome_permutation(self):
		for [test_string, expected] in self.data:
			result = is_palindrome_permutation(test_string)
			self.assertEqual(result, expected)

if __name__ == "__main__":
	unittest.main()
	
# Heavily influenced by solution and Python examples noted in README