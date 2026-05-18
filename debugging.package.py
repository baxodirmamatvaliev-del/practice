'''Debugging & package
(1) Python peckages & core package
(2) Package menager & externial peckage
(3) Debbuging
'''

import turtle
print("===========Python peckages & core package ========== ")
''' Python peckages/ Modules: core,file and extrnial'''
# core peckages https://docs.python.org/3/library

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.circle(170)

turtle.done

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
