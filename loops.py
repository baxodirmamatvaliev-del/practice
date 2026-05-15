''' loop operators
   (1) - for
   (2) - (break/else)
   (3) - while 
'''
# itarable object >> string , dict,tuple,list,range,map,filter <--- takrorlanish hususuyatiga ega bolgan obj xisobladi

import random
print("========== for operators ============")

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brend="Ferari ", yerar=2025)
range_obj = range(5)

# for  ketma ketlik aniq bolganda ishlaydi, while bolsa ketma ketlik aniq bolmagan paytda ishlaydi

for letter in text:
    print(f"the-letter:{letter}")

print("-----------")

for number in numbs:
    print(f"teh number: {number}")

print("---------")

for key in car_obj:
    print(f"the car key: {key} value => {car_obj.get(key)} ")

print("---------")

for x in range_obj:
    print(f"teh element: {x}")


print("========= break/else ========")

for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("reached break")
    break
else:
    print("Executed successfuly:)")


print("========= while operator ========")

numb = 40

while numb > 0:
    numb -= 10
    print(f"the number: {numb}")


print("-------")

x = random.randint(0, 100)

attempt = 0


while True:
    numberr = int(input("raqamni toping_"))
    attempt += 1

    if numberr > x:
        print("notog'ri: lekin kiritgan raqmingizdan kichkina!")
    elif numberr < x:
        print("notog'ri: lekin kiritgan raqamingizdan katta!")
    else:
        print(
            f"wow qoyil xaqiqatan ham {x} edi. siz {attempt} urinishda toptingiz :)")
        break
