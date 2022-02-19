"""
Checking for keys in a dictionary
"""

# print("Using 'in")
# print("=========")
#
mapping = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}
#
# # Keys
# print(1 in mapping)
# print(8 in mapping)
#
# # Values
# print(5 in mapping)
# print(-3 in mapping)
#
# # Both
# print(22 in mapping)

"""
protecting from errors
"""

keys = [8, 14, 22, 25]

# for key in keys:
#     print(key, mapping[key])

for key in keys:
    if key in mapping:
        print(key, mapping[key])
    else:
        print("{} not in mapping".format(key))
        
print("")


