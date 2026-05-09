''' FUNCTION
(1) DEFINE - CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''
print("===== define & call =====")
# build in function  > print() type()

# function - malum bir mantiqni ishga tushurib beradiga n code block:
# JAVA Function tuzish {}, Python da esa indentation tushuncha orqari tuzamiz!

# Define.   [a] parametr


def great(a):
    print(f"how do you do , {a}")


def greeting(b):
    print("greeting is executed:")
    return f"hi {b}"


# Call - execute
    # [LEO] argument:
result1 = great("LEO")
print("result1:", result1)
# [khan] argument:
result2 = greeting("KHAN")
print("result2:", result2)


print("========= Keyword & default arguments =========")

# DEFINE


def give_greet(name, age=26):
    print("give_greet is exsecuted")
    return f"hii {name}, you are {age} years old!"


result3 = give_greet(name="Leo", age=20)
print("result3:", result3)


result4 = give_greet("John")
print("result4:", result4)
