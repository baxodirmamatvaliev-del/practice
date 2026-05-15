
''' OPERATOR & CONDITIONS
(1) operatos 
(2) condition
(3) logical operatorss
'''
# referens tekshiryotganimizda maxsusu " is " operatori taqdim etilgan ekan:
# + - > < <= == *  is / // % += -= **

a = 19
b = 5

print(a / b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b**2", b**2)
print("b**3", b**3)

print("==**5")

c = dict(name="Martin", age=35)
# Pythonda referens emas tenglik yani value solishtiriladi
# ikkovi teng bolsa True teng bolmasa False
d = dict(name="Martin", age=35)
e = c

print("c==d", c == d)
print(id(c), id(d), id(e))


print("c is d", c is d)
print("c is e", c is e)


print("===== condition =====")

x = 15

if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")

print("------------")

print("=========== logical operators ===========")
age = 21

# persone = None
# if age > 17:
#   persone = "adult"
# else:
#  persone = "minor"


# ternary
persone = "adult " if age > 18 else "minor"

print("result:", persone)


is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("welcome here, do you want to be student")
elif is_admin:
    print("please go to office!")
elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")
