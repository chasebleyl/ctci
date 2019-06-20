# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. 
# O(ab) (but really O(N) since the size of a and b are +/- 1)

import unittest

def is_one_away(string_one, string_two):
  len_string_one = len(string_one)
  len_string_two = len(string_two)
  # String length difference must be <= 1 (4 & 4, 3 & 4, 5 & 4). If > 1 difference, return False
  if abs(len_string_one - len_string_two) > 1:
    return False
    
  max_differences = 2 if (len_string_one + len_string_two) % 2 == 0 else 1
  difference_count = 0
  table = [0 for _ in range(ord('z') - ord('a') + 1)]
  # If there are odd number of total characters, max differences <= 1
  # If there are an even number of total characters, max differences <= 2
  for char in string_one:
    char_index = get_char_index(char)
    if char_index != -1:
      table[char_index] = toggle(table[char_index])
      if table[char_index] == 1:
        difference_count += 1
      else:
        difference_count -= 1
  for char in string_two:
    char_index = get_char_index(char)
    if char_index != -1:
      table[char_index] = toggle(table[char_index])
      if table[char_index] == 1:
        difference_count += 1
      else:
        difference_count -= 1
  
  return difference_count <= max_differences

def get_char_index(char):
  a = ord('a')
  z = ord('z')
  A = ord('A')
  Z = ord('Z')
  char_value = ord(char)
  
  if a <= char_value <= z:
    return char_value - a
  elif A <= char_value <= Z:
    return char_value - A
  return -1
  
def toggle(previous_bit):
  if previous_bit == 0:
    return 1
  return 0

class Test(unittest.TestCase):
	'''Test Cases'''
	data = [
		('pale', 'ple', True),
		('pales', 'pale', True),
		('pale', 'bale', True),
		('pale', 'bake', False),
		('plate', 'pat', False),
		('pat', 'plates', False),
		('aba', 'baa', True),
	]
	
	def test_one_away(self):
		for [string_one, string_two, expected] in self.data:
			result = is_one_away(string_one, string_two)
			self.assertEqual(result, expected)

if __name__ == "__main__":
	unittest.main()