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


print("====== set in dictonariy comprehension ======")

numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}  # a-version
print("set_numbs:", set_numbs)

disc_people = {persone[0]: persone[1] for persone in people}  # b-version
print("disc_person:", disc_people)


disc_people2 = {persone[0]: persone[1]
                for persone in people if persone[1] > 20}  # b-version
print("disc_person2:", disc_people2)
