# Hash Tables

Hash Tables map keys to values for efficient look-ups (typically O(1) runtime). Hash tables work by:

1. Computing the key's hash code (typically an int or long)
2. Map that hash code to an index of the array
3. At the resulting index, store the key and value

There can be multiple keys that map to the same index, so each index has a Linked List which can have multiple key-value pairs. The better the hash function, the better the runtime and lookup will end up being.

## Hash Tables in Python

Hash Tables are represented in Python as dictionaries. For this exercise we will create a representation of Hash Tables using a Python Class, but typically we would use an ordinary dictionary to achieve a more efficient result.
