"""
Dictionary creation
"""

print("Dictionary Literals")
print("===================")

# Dictionary Literals

empty = {}
# print(empty)

simple = {1: 1}
print(simple)

squares = {1: 1, 2: 4, 3: 9, 4: 16}
print(squares)

cipher = {'p': 'o', 'y': 'h', 't': 'n', 'h': 't', 'o': 'y', 'n': 'p'}
print(cipher)

goodinstructors = {'Rixner': True, 'Warren': False}
print(goodinstructors)

print("")
print("Creating Dictionaries")
print("=====================")

empty = dict()
print(empty)

data = [(1, 'bfy'), (2, 'two'), (3, 'three')]
names = dict(data)
print(names)

cipher_dict = dict(cipher)
cipher['p'] = 'q'
print(cipher, cipher_dict)

