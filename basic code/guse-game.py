import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: easy, medium or hard")

level = input('Enter difficulty: '). lower()
if level == "easy":
    secret = random. choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("invelid input, defolt medium")
    secret = random.choice(medium_words)

while True:

    guess = input("Guess the spelling: ")

    if guess == secret:
        print("Congoooo")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint: ", hint)
print("Game Over")