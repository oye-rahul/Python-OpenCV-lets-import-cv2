# print("hello world")

# print("helo " * 10)

# x = 1
# z = 2
# print(x+z)

# x = int(input("Enter a number: "))
# print(x * 3.14)

# price = 99.9
# AfterDecunt = (price - (price * 10/100))
# print(round(AfterDecunt, 4))

# firstName = input("ent yur first name: ")
# lastName = input("ent yur last name: ")
# fullName = firstName +" "+ lastName
# dash = "-" * 35
# print(dash)
# print("| your fullname is: ", fullName ,"|")
# print(dash)

# age = 16
# can_vote = age >= 18
# print(can_vote)
# #ANS is come in false and true (flase is ans)

# FixAge = 18 
# MyAge = int(input("entar your age: "))
# # laisn = True
# oatho = FixAge < MyAge
# print(oatho)

# # ------------------------------------------------------

# name = "rahul"
# string = f"is player name is {name}"
# print(string)
# print (name.upper())
# print (name.lower())
# print (string.title())

# #check is something is exists
# print("rahul" in string) #T & F
# print(string.startswith("player")) #T & F
# print(string.endswith("rahul")) #T & F

# #find position
# print(string.find("name"))
# print(string.count("is"))

# #replays 
# new_string = string.replace("rahul", "zozo")
# print(new_string)
# # ------------------------------------------------------

# #if
# bln = 500
# pin = 123 
# if pin == 123:
#     print("curret")

# #if else
# if pin == 000:
#     print("currt")
# else:
#     print("incrrt")

# #elif 
# password = int(input("entar your password: "))
# if password == 123:
#     print("welcome user")
# elif password != 123:
#     print("check your pin")
# else:
#     print("try again")

# mark = int(input("entar your marks: "))

# if mark >= 90:
#     print("A")
# elif mark >= 80:
#     print("B")
# elif mark >= 70:
#     print("C")
# elif mark >= 60:
#     print("D")
# elif mark >= 50:
#     print("E")
# else:
#     print("F")

# age = int(input("entar your age: "))
# has_license = True
# not_license = False
# #both must be TRUE
# if age >= 18 and has_license:
#     print("u can drive")
# else:
#     print("u cant")

# v = int(input("entar your vahical typ ex.'2-4': "))
# #at least one is True (in this 2 wheelr are alw)
# if v == 2 or not_license:
#     print("u can drive")
# else:
#     print("u cant")

# if not age >= 18:
#     print("you are underage")
# else:
#     print("yes, u can")

# # for loop
# for i in range(1,6):
#     print(i)
# # 1,2,3,4,5

# for i in range(1,11,2):
#     print(i)
# #1,3,5,7,9
# line = "----------------------------"
# name_list = ["rahul","zozo","tont","rox","memo"]
# #get item
# print(line)
# print(name_list[2])
# print(name_list[-1])
# #slicing
# print(line)
# print(name_list[0:1])
# print(name_list[:4])
# print(name_list[1:])
# #chnge
# print(line)
# name_list[0] = "Golu"
# print(name_list)
# #add
# print(line)
# name_list.append("golaa")
# print(name_list)
# name_list.insert(1, "xoxo")
# print(name_list)
# # remove
# print(line)
# name_list.remove("tont") #by value
# print(name_list)
# name_list.pop() #by last word 
# print(name_list)
# del name_list[1] #by value
# print(name_list)

# # num shoerting (.sort() .reverse(), .copy())
# num = [1,5,8,4,7,3,1,2,0,4,7]
# num.sort()
# print(num)

# person = {
#     "name" : "rahul",
#     "age" : 20,
#     "city" : "ahm"
# }
# print(person["name"])
# person["laptop"] = "victus"
# del person["city"]
# print(person)

# print(person.keys())
# print(person.values())
# print(person.items())

# person.update({
#     "age": 30,
# })
# print(person)