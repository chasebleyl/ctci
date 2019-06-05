# ArrayList

class ArrayList:
    def __init__(self):
        self._size = 5 # Starting size will be 10
        self._insertion_index = 0
        self._array_list = [None] * self._size
        
    def append(self, element):
        if self._size == self._insertion_index:
            self._expand()
        self._array_list[self._insertion_index] = element
        self._insertion_index += 1
        
    def length(self):
        return len(self._array_list)
        
    def print_length(self):
        print(len(self._array_list))
        
    def print_array(self):
        print(">>> Printing contents:", self._array_list)
        
    def _expand(self):
        self._size = self._size * 2
        new_array = [None] * self._size
        i = 0
        while i < len(self._array_list):
            new_array[i] = self._array_list[i]
            i += 1
        self._array_list = new_array
        
new_list = ArrayList()
new_list.print_array()
new_list.append(1)
new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(5)
new_list.print_length()
new_list.append(6)
new_list.print_length()
new_list.append(7)
new_list.append(8)
new_list.append(9)
new_list.append(10)
new_list.print_length()
new_list.append(11)
new_list.print_array()
new_list.print_length()