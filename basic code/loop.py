#table

# n = int(input("Enter your table number: "))
# for b in range(1, 11):   # 1 se 10 tak loop
#     i = n * b            # har step ka result
#     print(f"{n} x {b} = {i}")

# n = int(input("entr you table number: "))
# for i in range(n, (n*10)+1, n):
#     print(i)

# n = int(input("entr you table number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# n = int(input("entr you number: "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print("even", even)
# print("odd", odd)

# n = int(input("entr you number: "))
# cn = []
# for i in range(1,n+1):
#     if n % i == 0:
#         cn.append(i)
# print(cn)

# n = int(input("entr you number: "))
# cn = 0
# for i in range(1,n-1):
#     if n % i == 0:
#         cn = cn + i
#
# if cn == n:
#     print("your number if perfect", cn)
# else:
#     print("your number is not perfect, X",cn)

# n = int(input("entr you number: "))
# pn = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         pn = pn + 1

# if pn == 2:
#     print("YES, your number is prime", pn)
# else:
#     print("NO, your number is not prime, X",pn)

import random
rnum = random.randint(1,100)
t = 0
while True:
    unum = int(input("ent your number between 1 - 100: "))
    if rnum == unum:
        t = t + 1
        print("WIN !!!")
        break
    elif unum < rnum:
        t = t + 1
        print("try higger")
    elif unum > rnum:
        t = t + 1
        print("try lesser")
    else:
        t = t + 1
        print("input is wrong")

print(f"""WOW! your win this game number {rnum} = {unum} and 
---------you take {t} tryles--------- """)

