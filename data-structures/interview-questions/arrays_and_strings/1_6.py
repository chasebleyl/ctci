# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
# O(N)

import unittest

def compress_string(string):
  prev_char = string[0]
  repeat_count = 1
  compressed_chars = [string[0]]
  for i in range(1, len(string)):
    if string[i] == prev_char:
      repeat_count += 1
    else:
      compressed_chars.append(str(repeat_count) + string[i])
      repeat_count = 1
      prev_char = string[i]
  compressed_chars.append(str(repeat_count))
  
  compressed_string = ''.join(compressed_chars)
  if len(compressed_string) < len(string):
    return compressed_string
  return string

# First attempt, string concatenation is inefficient so needed to upgrade
# def compress_string(string):
#   prev_char = string[0]
#   repeat_count = 1
#   compressed_string = string[0]
#   for i in range(1, len(string)):
#     if string[i] == prev_char:
#       repeat_count += 1
#     else:
#       compressed_string += str(repeat_count) + string[i]
#       repeat_count = 1
#       prev_char = string[i]
#   compressed_string += str(repeat_count)
  
#   if len(compressed_string) < len(string):
#     return compressed_string
#   return string

class Test(unittest.TestCase):
	'''Test Cases'''
	data = [
		('abbcccdddd', 'a1b2c3d4'),
		('aabbccdd', 'aabbccdd'),
		('aaAAAaa', 'a2A3a2'),
		('abc', 'abc'),
	]
	
	def test_compress_string(self):
		for [string, expected] in self.data:
			result = compress_string(string)
			self.assertEqual(result, expected)

if __name__ == "__main__":
	unittest.main()