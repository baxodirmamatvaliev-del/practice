'''Debugging & package
(1) Python peckages & core package
(2) Package menager & externial peckage
(3) Debbuging
'''

from PIL import Image
# pillow. package orqari bis rasimning size va razmerini bera olar ekanmiz.
import turtle
print("===========Python peckages & core package ========== ")
''' Python peckages/ Modules: core,file and extrnial'''
# core peckages https://docs.python.org/3/library

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(170)

# turtle.done

my_file = open("material/message.txt", "r")

try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()


with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content", your_content)

print("DONE")


print("========== Package menager & externial peckage ==========")
''' peckage meagers: pip pipenv npm yarn comproser brew'''
# externial peckage https://pypi.org/


with Image.open("material/2.jpg") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.show("material/sample.png")

print("=========== Debbuging ===========")
# Debbuging. orqari biz xatolarni bir zumda topip ,jarayonni
# huddi mashina oylayotgan singari kuchli taxlilni amalga oshirishimiz
# mumkin bolar ekan.


def get_summary(*args):   # DEFINE
    total_amount = 0

    for a in args:
        total_amount += a

        return total_amount


result = get_summary(1, 2, 3, 4, 5)   # CALL
print("result:", result)
