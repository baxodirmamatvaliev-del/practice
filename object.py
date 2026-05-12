
'''
(1) Object ozi nima
(2) Iteralble objects & RANGE 
(3) DICTIONARY
(4) error hadling tizimi 
'''

import array  # package/method
import math
from math import ceil
print("================ object ozi nima ===================")
# object lar ozini mahsus state va method lariga ega borgan propertilarga ega !
# Python da hamma narsa obeject !
print(type(math))
print(type(" hello world"))
print(type(300))
print(type(array))
print(type(True))

result1 = math.ceil(97.7)
print("result1", result1)

print("=========== error hadling sistem=============")

car_dict = dict(name="Porse", year=2026, electric=False)


try:
    print("passed hear:")
    a = car_dict.speed
    result1 = car_dict["origin"]
    print("result1:", result1)
except KeyError as err:
    print("no origin state propirty found:", err)
except AttributeError as err:
    print("no spead found:", err)
else:
    print("exsucuted succsessfuly withoun errors")
finally:
    print("finaly closing ligic ")
