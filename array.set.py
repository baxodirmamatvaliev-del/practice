''' Array & Set
   (1) Array
   (2) Set
   (3)Specific Operators with set
'''

from array import array

print("=========== Array ============")

# ARRAY LARNI BIZ XAR DOIM HAM ISHLATAVERMAS EKANMAIZ, FAQATGIN MAXSUS BOLGAN VA MALUMOYIMMIZ
# KOP BOLSA GINA ISHLATAR EKANMIZ, QOLGAN PAYTLAR ESA ARRAY NI ORNIGA LISTLAR HAM
# BIZNI ISHIMIZNI BAJARAVERAR EKAN.


numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1)", numbers)


# append(). ni  text oxiridan malumot koshishda ishlatamiz
numbers.append(100)
# inseert(). esa bu oldidan yani 0-INDEX ga qoshib beradi
numbers.insert(0, 14)
print("numbers(2)", numbers)
# remove(), biz belgilagan valueni ochirib beradi
numbers.remove(5)
# pop(), malumotizmizdan ohirgi valueni ochirib tashlaydi
numbers.pop()
print("numbers(3)", numbers)

del numbers[0:2]
print("numbers(4)", numbers)

print("=========== Set =========")  # QISQA: TAKRORLANMAYDIGAN TOPLAM!
# SET NI BIZ TAKRORIY BOLISHI KERAK BOLMAGAN PAYTLARDA ISHLATAR EKANMIZ,
# YANI ARRAY ICHIDA BITTA VALUE 2-MARTA QATNASHGAN BOLSA "SET" BIZGA UNI
# 1-MARTA OLIB BERADI. BIZ "SET" NI SHUNDAY PAYTLARDA ISHLATAR EKANMIZ.
# VA "SET" INDEX YANI  KETMA KETLIK BOLMAYDI.

new_numbers = array("i", [1, 4,  5,  7, 8, 41])
numbs_set = set(new_numbers)

print(f" the numbs set: {numbs_set} and type: {type(numbs_set)}")


# SET ni ozini Method lari bor ekan.


# add(). bu oxiridan value qoshib berar ekan
numbs_set.add(200)
print("numbs_set(1)", numbs_set)

numbs_set.add(7)
print("numbs_set(2)", numbs_set)


print("========== Specific Operators with set. |,&,-,^")

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
# union degani har 2-ikkala toplamdagi qiymatlarni bir
# set ga toplab berar ekan.va albatta 2-marta takrorlangan qiymatlarni takrorlamas ekan. va natija {50, 20, 40, 10}
print("result1:", result1)

result2 = a & b  # intersection
# intersection degani "a" ning va "b" ning ichida mujassam bolgan degani.
# yani "a" va "b" ni ichida takrorlangan sonni korsat degan mantiqni bajaradi. va natija {20}
print("result2:", result2)

result3 = a - b  # deferance
# "a" va b da bolgan qiymatlar olib tashlanadi va "b" ni qoymati otmaydi. va natija: {10, 50}
print("result3:", result3)

result4 = a ^ b  # symetric deference
# symetrix deference bu dgani, bir birda qatnashgan qiymatlarni olib tashlayi, yani 20-ma chuni 2-marta qatnashgan
# va qatnashmagan qiymatlarni olib beradi. yani {40, 10, 50}

print("result4:", result4)
