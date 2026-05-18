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
