'''Comprahansion
  (1) What ic Comprahansion & list compp
  (2) set in dictonariy comp.
'''

print("====== What ic Comprahansion & list comprahansion ======")
# COMPRAHANSION DEGANI SPREAD DGANNI,BOSHQA TILLARDAGI SPREAD "PYTHON" DA COMPRAHANSION DGANI!

''' Comprahansion
   (a) *itarable
   (b) <expression> for item in itarable
   (c) <expression> for item in itarable <condition>
'''

numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a-version
print("list_numbers", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("--------")
people = [("Robert", 21), ("Stave", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b-version
print("list_people:", list_people)

cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars", list_cars)
