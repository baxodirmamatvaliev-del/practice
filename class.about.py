
'''
(1) class ozi nima
(2)ordinary va static properties   #static properties " BULAR TOGRIDAN TOGRI CLASS BILAN KELADIGAN state yoki method LAR HISOBLANADI
(3) maxsus method
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


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args, **kwargs):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("-------")

your_car = Car("Toyota", 2026)
print(your_car)
response = your_car()
print("response:", response)


# MITASK G
def mitask(numbers):

    kuch = 0

    for i in range(len(numbers)):
        if numbers[i] > numbers[kuch]:

            kuch = i

    return kuch


savatcha = [1, 45, 1, 44, 4]
print(mitask(savatcha))
