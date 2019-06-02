# Hash Table implementation
#
# Followed tutorial located at https://www.youtube.com/watch?v=9HFbhPscPU0

class HashTable:
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size

	def _get_hash_code(self, key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size

	def add(self, key, value):
		key_hash = self._get_hash_code(key)
		key_value = [key, value]

		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		for pair in self.map[key_hash]:
			if pair[0] == key:
				pair[1] = value
				return True
		self.map[key_hash].append(key_value)
		return True

	def get(self, key):
		key_hash = self._get_hash_code(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None

	def delete(self, key):
		key_hash = self._get_hash_code(key)
		if self.map[key_hash] is None:
			return False
		for i in range (0, len(self.map[key_hash])):	
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True
		return False

	def print(self):
		print('----BIRTHDAYS----')
		for item in self.map:
			if item is not None:
				print(str(item))

h_table = HashTable()
h_table.add('Bob', '1965-10-21')
h_table.add('Anne', '1973-07-25')
h_table.add('Manny', '1985-02-13')
h_table.add('Milinda', '1915-12-03')
h_table.add('Marlon', '1917-04-21')
h_table.add('Keir', '1959-10-11')
h_table.add('Carl', '1988-01-27')
h_table.add('Darnell', '1967-07-10')
h_table.add('Harris', '1984-04-24')
h_table.add('Fred', '1994-08-20')
h_table.print()
print("Before:", h_table.get('Carl'))
h_table.add('Carl', '1998-12-31')
print("After:", h_table.get('Carl'))
h_table.delete('Carl')
print("Deleted Carl")
h_table.print()
