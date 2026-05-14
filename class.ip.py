''' class chuqur organamiz
   ( CONCEPTS. (4) )
   (1) Abtiraction
   (2) Encapsulation
   (3) Inheritense
   (4) Polimorphism
'''
print("========== inheritense ===========")

# parent ozini public va protectet bolgan propertilarni meros qila olar ekan. private bolsa esa meros qilmas ekan!


class Animal:  # perent
    description = "This class is parent for animals"

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # chiled

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}-{self.sound}")

    def protect(self):
        print("yes ,I can protect you!")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}-{self.sound}")

    def swim(self):
        print("yes ,I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "Zzzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("---------")

dog.make_voice()
fish.make_voice()
cat.make_voice()

print("--------")

print(Animal.description)
print(fish.description)

print(dog.voice, fish.voice)
