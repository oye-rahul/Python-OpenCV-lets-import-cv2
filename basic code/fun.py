#create a funtion
# def funtionName():
#     print("all code")
# #calling funtion
# funtionName()

# def true():
#     print("number match")
# def false():
#     print("number is not match")

# a = int(input("num1 :"))
# b = int(input("num2 :")) 
# if a == b:
#     true()
# else:
#     false()

# def chkNum (num1,num2,Fname,Lname,age=20):
#     if num1 == num2:
#         print(f"name is {Fname} {Lname} {age} | equil", num1 ,"=", num2 )
#     else:
#         print("not equil")
# chkNum(5,5,Lname="malvi",Fname="rahul",age=18)
# chkNum(5,5,"rahul","malvi")

# def cal (price,taxRt,discount):
#     tax = taxRt / 100
#     maintax = price * tax
#     AfterTex = price + maintax
#     maidiscount = AfterTex / discount
#     finalprice = AfterTex - maidiscount
#     print("-------------------------")
#     print(f"Total Bill is: ${finalprice}")

# price1 = int(input("Price: "))
# tax1 = int(input("Tax: "))
# dic1 = int(input("Discount: "))
# cal(price1,tax1,dic1)

# fname="malvi"
# def name (lname):
#     print(fname,lname)
# name ("rahul")

from datetime import datetime
nows = datetime.now()
print(nows)

import datetime
today = datetime.date.today()
print(today)

import os
currntOS = os.getcwd()
print(currntOS)

import json
data = {"name":"rahul","age":20}
jstring = json.dumps(data)
print(jstring)


