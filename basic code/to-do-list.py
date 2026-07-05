print("----This is To-Do List----")

print("""
For Add Item-1,
For View All items-2,
For Delete Item-3,
For Exit-4.

Choose Any Task to Perform
""")

choice = input("enter Your Choice: ")

if choice == '1':
    file = open("TD.txt", "a")