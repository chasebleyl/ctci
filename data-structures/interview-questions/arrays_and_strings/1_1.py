# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hints: #44, #117, #132

unique_strings = [ 'abc', 'ABC', 'abA', 'abAB', '123', '1a2b', 'abcdefg' ]
non_unique_strings = [ 'aba', 'ABA', 'abab', '1212', 'abcdefga' ]

def validate_strings(string_array, expected_result):
	for string in string_array:
		result = unique_string(string)
		if result != expected_result:
			print("For string " + string + " expected " + str(expected_result) + " but got " + str(result))

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

validate_strings(unique_strings, True)
validate_strings(non_unique_strings, False)

print("Finished validating strings!")

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
