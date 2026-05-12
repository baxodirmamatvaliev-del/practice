print("=========== Iteralble objects & RANGE ==========")
# itarable object >> string , dict,tuple,list,range,map,filter

range_obj = range(3)
print("range_obj", range_obj)

for letter in "MIT":
    print(f"the letter:{letter}")


for ele in range_obj:
    print(f"the element: {ele}")

print("=========== DICTIONARY============")

person = {"name":  "Justin", "age": 24, "single": True}
persone_obj = dict(name="Justin", age=24, single=True)

print("person:", person)
print("persone_obj:", persone_obj)

name = persone_obj.get("name")
hobby = persone_obj.get("hobby")
balance = persone_obj.get("balance", 0)

print(f"the name {name} , hobby is {hobby} , and balance {balance}")

del persone_obj["single"]
for key in persone_obj:
    print(f"the key: {key} >> value {persone_obj.get(key)} ")
