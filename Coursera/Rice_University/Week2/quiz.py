import numpy as np

# One

my = {'name': 1, 'address': 2}
print('names' in my.keys())

#  my_key in my_dict.keys()

# Two

# my_dict.items()

# Three
# my_matrix[1][4]

# The expression \color{red}{\verb|my_dict[25]|}my_dict[25] raises a KeyError since 2525 is not a valid key while the
# expression \color{red}{\verb|my_dict.get(25)|}my_dict.get(25) returns \color{red}{\verb|None|}None in this case.

NUM_ROWS = 3
NUM_COLS = 5

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)

# print the matrix
for row in my_matrix:
    print(row)

print(my_matrix[1][4])

num = 0
c = 0
while c <= 24:
    num += c * c
    c += 1

print(num)

# five
# 4324

# six dictionaries of lists
{'a': ['a', 'b', 'c'], 'b': ['b', 'c', 'd'], 'c': ['c', 'd', 'e']}

# seven
one = {2: {6: 12, 2: 4, 0: 0, 7: 14, 5: 10, 3: 6, 8: 16, 4: 8, 1: 2},
       4: {0: 0, 3: 12, 2: 8, 6: 24, 4: 16, 5: 20, 8: 32, 7: 28, 1: 4},
       1: {2: 2, 5: 5, 3: 3, 8: 8, 4: 4, 1: 1, 7: 7, 0: 0, 6: 6},
       3: {4: 12, 0: 0, 8: 24, 6: 18, 7: 21, 3: 9, 5: 15, 1: 3, 2: 6},
       0: {8: 0, 1: 0, 6: 0, 2: 0, 4: 0, 5: 0, 3: 0, 0: 0, 7: 0}}
# two = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 2, 4, 6, 8, 10, 12, 14, 16],
#        [0, 3, 6, 9, 12, 15, 18, 21, 24], [0, 4, 8, 12, 16, 20, 24, 28, 32]]
three = {1: {1: 2, 7: 2, 3: 2, 8: 2, 0: 2, 5: 2, 2: 2, 6: 2, 4: 2},
         2: {5: 4, 1: 4, 8: 4, 0: 4, 3: 4, 2: 4, 4: 4, 7: 4, 6: 4},
         3: {4: 6, 2: 6, 1: 6, 5: 6, 0: 6, 7: 6, 8: 6, 3: 6, 6: 6},
         0: {0: 0, 5: 0, 6: 0, 8: 0, 1: 0, 3: 0, 2: 0, 4: 0, 7: 0},
         4: {3: 8, 8: 8, 7: 8, 5: 8, 4: 8, 1: 8, 2: 8, 6: 8, 0: 8}}
four = {1: {7: 7, 4: 4, 3: 3, 8: 8, 6: 6, 5: 5, 2: 2, 0: 0, 1: 1},
        0: {0: 0, 7: 0, 3: 0, 4: 0, 8: 0, 6: 0, 5: 0, 1: 0, 2: 0},
        2: {0: 0, 8: 16, 5: 10, 2: 4, 7: 14, 4: 8, 1: 2, 3: 6, 6: 12},
        3: {1: 3, 7: 21, 2: 6, 8: 24, 3: 9, 4: 12, 6: 18, 0: 0, 5: 18},
        4: {3: 12, 7: 28, 0: 0, 2: 8, 1: 4, 4: 16, 6: 24, 5: 20, 8: 32}}

NUM_ROWS = 5
NUM_COLS = 9


def check(dict1):
    for row1 in range(NUM_ROWS):
        for col1 in range(NUM_COLS):
            if dict1[row1][col1] != row1 * col1:
                return False

    return True


print(check(one))
# print(check(three))
# print(check(four))

# # construct a matrix
# my_matrix = {}
# for row in range(NUM_ROWS):
#     row_dict = {}
#     for col in range(NUM_COLS):
#         row_dict[col] = row * col
#     my_matrix[row] = row_dict
#
# print(my_matrix)
#
# # print the matrix
# for row in range(NUM_ROWS):
#     for col in range(NUM_COLS):
#         print(my_matrix[row][col], end=" ")
#     print()

# {2: {6: 12, 2: 4, 0: 0, 7: 14, 5: 10, 3: 6, 8: 16, 4: 8, 1: 2}, 4: {0: 0, 3: 12, 2: 8, 6: 24, 4: 16, 5: 20, 8: 32, 7: 28, 1: 4}, 1: {2: 2, 5: 5, 3: 3, 8: 8, 4: 4, 1: 1, 7: 7, 0: 0, 6: 6}, 3: {4: 12, 0: 0, 8: 24, 6: 18, 7: 21, 3: 9, 5: 15, 1: 3, 2: 6}, 0: {8: 0, 1: 0, 6: 0, 2: 0, 4: 0, 5: 0, 3: 0, 0: 0, 7: 0}}
