""" List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumerate, map and filter
"""

print("===== Working with lists =====")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constructor
result = list("Hello World!")
# <--len() , text size ni olib beradi:
print(f"the result: {result} and size: {len(result)}")


print("------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # 0-1 index dagi valuen ni yani qiymatni ol degani  [0, 2)
# 3 index gacha bolgan valueni olib ber 3 index dagini olma dgani
c = fruits[:3]
d = fruits[::-1]  # value ni yani qiymatni teskari olib beradi (::-1)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# list bu obj, obj esa ozini state va method lariga ega bolgan datatype xisoblanadi


print("======  List methods =======")
# method -> Mytble: append(), inseert(), pop(), remove(), clear(), sort(),
#
#  index().


letter = ["a", "b", "c"]
# append(). ni  text oxiridan malumot koshishdsa ishlataiz
letter.append("d")
print(f"the append result: {letter}")

letter.insert(0, "m")
# inseert(). esa bu oldidan yani 0-INDEX ga qoshib beradi
print(f"the inseert result: {letter}")


size = len(letter) - 1
# pop(). esa bu biz belgilagan index dan vaueni olib tashlaydi
result1 = letter.pop(size)
print(f"the pop result1: {result1} and letters: {letter}")


result2 = letter.pop(0)
print(f"the pop result2: {result2} and letters: {letter}")

print("------")

animals = ["dog", "cat", "capybara", "fish", "lion"]
print(f"animals:", animals)

animals.remove("lion")
# remove(). bu ochirib yani remove qlib berabr ekan
print(f"the animals remove result: {animals}")

del animals[2:4]
print("del result:", animals)

exist = animals.index("cat")
# index(). bu biz qidirgan qiymat bormi yoqmi shuni tekshirib beradi bor bolsa index orqari qaytaradi
print("the exist:", exist)

animals.clear()
# animals(), bu hamma value larni tozalab berar ekan
print("the animals clear:", animals)

if "cat" in animals:
    print(f"index off cat: ", animals.index("cat"))
else:
    print("cat does not exist")


print("---------")

numbers = [2, 20, 12, 8, 57]
# sort(). bizni parametr larimizni tartiblab berar ekan.
numbers.sort()
print("the numbers sort:", numbers)

numbers.sort(reverse=True)
# sort() ning reverse tushunchasi bu tartiblangan sonlarni teskarisiga ogirib berar ekan
print("sort, reverse:", numbers)

# imutble sorted
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs {new_numbs}")


print("======= Lambda function =======")
# lambda kichik anonim function


def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]

people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)

# enumerate for index & value

animals = ["dog", "cat", "fish"]  # list
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

print("-------")
# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025)  # dict
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {key} and value: {value}")

print("-------")
# map
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

result_map = map(lambda car: car[0], cars)
print(f"the result_map: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars", new_cars)

print("-------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
