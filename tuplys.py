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

print("========= Unpacking arguments =========")

groups = ["MIT", "FLEX", "DEVEX", "MG"]


(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
calculate(0, 2, 300)
calculate(5, 7)

print("-----")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs['name']} and I am {kwargs['age']} years old!")
    pass


# CALL
introduce(name="Justin", age=28)
introduce(name="Shawn", age=30, single=True)


print("-----")


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# CALL
greeting("hi", True, 10, name="John", age=22)


print("===== zip =====")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
result = list(zipped)
print(f"the result: {result}")
