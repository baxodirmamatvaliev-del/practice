''' Tuple
    (1) What is tuple: type vs list
    (2) Unpacking arguments
    (3) zip
'''

print("====== What is tuple: type vs list =====")
# Java/PHP/NodeJS array => Python list

# literal
numbs = [3, 5, 1, 2]

# constructor
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# we can not mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"
