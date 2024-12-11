# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper
# @decorator
# def say_hello():
#     print("Hello")
# say_hello()

import copy

# original = [[1, 2], [3, 4]]
# shallow = copy.copy(original)
# deep = copy.copy(original)

# shallow[0][0] = 99
# deep[1][0] = 88

# print(original)
# print(deep)

# a = [1, 2]
# b = [1, 2]

# print(a==b)
# print(a is b)

import copy
original = [[1,2], [3,4]]
deep = copy.deepcopy(original)
print(deep)