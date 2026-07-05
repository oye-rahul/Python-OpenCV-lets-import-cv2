a = int(input("enter your age: "))

print("\n-------if else-----")
if(a < 18):
    print("tu chota he 18 sal se ghadhe")
else:
     print("tu bada he 18 sal se")

print("\n-------elif-----")
if(a < 13):
    print("you are not teenager")
elif(a < 18):
    print("you are teenager but not adult")
else:
    print("you are adult")