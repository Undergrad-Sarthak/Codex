import random


def guesser(num):
    tries = 0
    while True:
        guess = int(input("Make a guess: "))
        tries += 1
        if guess == num:
            print("You guessed correct")
            print("Took you", tries, "tries to guess it correct")
            break
        elif guess > num:
            print("try a smaller number")
        else:
            print("try a bigger number")


print("Welcome to Number guesser")
print("Choose your difficulty:")
print("1: numbers 0-10")
print("2: numbers 0-100")
print("3: numbers 0-1000")
limit = input("1,2,3 -> ")


if limit == "1":
    number = random.randint(0, 10)
    guesser(number)
elif limit == "2":
    number = random.randint(0, 100)
    guesser(number)
elif limit == "3":
    number = random.randint(0, 1000)
    guesser(number)
else:
    print("Choose 1, 2 or 3")
