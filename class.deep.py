''' class chuqur organamiz
   ( CONCEPTS. (4) )
   (1) Abtiraction
   (2) Encapsulation
   (3) Inheritense
   (4) Polimorphism
'''

print("========  Encapsulation ========")

'''
 ("C++,JAVA,PHP...." Encapsulation )
C++ > JAVA > public - private - protected
PHP TypeScript > public - private - protected

 ( " Python " Encapsulation )
Python > public __private _protected

'''

# private satet & method larnini biz faqat Account class ichida ishlata olarmz®


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    # private bolgan payt owner malumotini olishimiz uchun (GETTER)) kerak boladi
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("new_ownership", self, new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("-------")

try:
    result = my_account.__amount
    print("reult", result)
except Exception as err:
    print(" no target state found!", err)


# getter vs setter
print("owner before ", my_account.holder)

# my_account.change_ownership("Martin")
my_account.holder = "Martin"

print("owner after", my_account.holder)
