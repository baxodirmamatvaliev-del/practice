# PRIMITIVE veruabls "number" "string" "buuling" hammasi object!

# Object lar ozini bir qator propirtilariga ega bolgan datatype hisoblanadi

print("====== number =======")

# JAVA + C _ tillarida: malumot manzilini nomlanishi:
# Python  _tilida: Referesning nomlanishi hisoblanadi:

count = 100
count_type = type(count)
print("count:", count)
print("count:", count, count_type)
print(f"the count: {count} and type: {count_type} ")

rusult1 = count.bit_count()  # method
result2 = count.numerator  # state

print(rusult1, result2)


# object lar kabi "string ham" ozini "state" va "method" ga ega ekan:
print("====== string =======")
# METHOD: upper() lower() title(). find() replase(). eng kop ishlatiladigan method lar:


course = "AI Python FullStack"
result = type(course)
print(f"the result (1): {result}")
# title method text bosh harifini katta harifda qlib beradi:
result = course.title()
print(f"the result (2):  {result}")
# upper method text hariflarini hammasini kattaharif qlib beradi:
result = course.upper()
print(f"the result (3): {result}")
# replace text sozlarini ozgartirib beradi:
result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")


print("====== boolean =======")
# FUNCTION > type() input() bool() int() str()
y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric {result}")


# . TRUTHY VS FARSY
# TRUTHY: True 100 -100 "MIT42"
# FALSY : False "" 0 None

test_falsy = "" or False or None or 100
print("the foulsy:", bool(test_falsy))


test_truthy = "MIT42"
print("the truthy:", bool(test_truthy))
