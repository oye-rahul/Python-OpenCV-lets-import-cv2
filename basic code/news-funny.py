import random

obj = ["Shahrukh Khan", "Virat Kohli", "Nirmala Sitharaman", "A Mumbai Cat", "A Group of Monkeys"]
action = ["launches", "cancels", "dances with", "eats", "declares war on"]
place = ["at Red Fort", "in Mumbai local train", "a plate of samosas", "inside Parliament", "at Ganga ghat"]

while True:
    fisrt = random.choice(obj)
    second = random.choice(action)
    thard = random.choice(place)

    print(f"BREAKING NEWS:- {fisrt} {second} {thard}")

    user = input("generate more news 'yes','no'.")

    if user == 'yes':
        print()
    else:
        print("GoodBy")
        break



