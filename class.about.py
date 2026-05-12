
'''
(1) class ozi nima
(2)ordinary va static properties   #static properties " BULAR TOGRIDAN TOGRI CLASS BILAN KELADIGAN state yoki method LAR HISOBLANADI
(3)
'''
print("============ class ozi nima ============")
# class lar object yasash uchun shablon hisoblanadi!
# structure 3x  >> constructor method state


class Person():
    # state
    message = "static  state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explans(cls):
        print("static method property esecuted:")


person1 = Person("Justin", 25)
person2 = Person("Martin", 38)
person3 = Person("John", 26)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("========== ordinary va static properties ==========")
#  #static properties " BULAR TOGRIDAN TOGRI CLASS BILAN KELADIGAN state yoki method LAR HISOBLANADI
new_message = Person.message
print("new_message:", new_message)

# static
