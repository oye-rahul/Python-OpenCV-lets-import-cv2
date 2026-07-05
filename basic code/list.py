# a = [-56,58,-9,89,5,8,-89,-41,-8]
# print("possitive number")
# for i in a:
#     if i > 0:
#         print(i)
# print("possitive number")
# for i in a:
#     if i < 0:
#         print(i)

# total = []   # list banani hogi
# while True:
#     unum = int(input("Enter number: "))
#     total.append(unum)   # input ko list me add karo

#     ask = input("Add more? y/n: ")
#     if ask.lower() == 'y':
#         print("ok add it")
#     else:
#         break
# num = 0
# for i in total:
#     num = num + i
# print("Sum =", num)

# list_of_number = []
# while True:
#     user_num = int(input("Enter Your number: "))
#     list_of_number.append(user_num)

#     user_ans = input("u want to add any number (y,n?")
#     if user_ans == 'y':
#         print()
#     else:
#         break
# method = input("""
# Which method you want to use it.
# press 1 for mean                             
# """)
# store_number = 0
# if method == '1':
#     for i in list_of_number:
#         store_number = store_number + i

#     print(store_number/len(list_of_number))

# num = [10,30,20,50,20,100,50,0,200]
# lrg = num[0]
# for i in range(len(num)):
#     if num[i] > lrg:
#         lrg = num[i]
# print(lrg)


# number = []
# while True:
#     unum = int(input("enter you number"))
#     number.append(unum)
#     ask = input("Add more? y/n: ")
#     if ask.lower() == 'y':
#         print()
#     else:
#         break
# option = input("""
# which number you want Large & Small
# for large = L,
# for small = S:                            
# """)
# Lnum = number[0]
# Snum = number[0]
# if option == 'L':
#     for i in range(len(number)):
#         if number[i] > Lnum:
#             Lnum = number[i]
#     print(Lnum)
# elif option == 'S':
#     for i in range(len(number)):
#         if number[i] < Snum:
#             Snum = number[i]
#     print(Snum)
# else:
#     print("plz enter velid input")

# num = [10,30,20,50,20,100,50,0,200]
# lrg = num[0]
# sec_lrg = num[0]
# for i in num:
#     if i > lrg:
#         sec_lrg = lrg
#         lrg = i
#     elif i > sec_lrg:
#         sec_lrg = i
# print(lrg, sec_lrg)








