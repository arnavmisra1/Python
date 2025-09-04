from random import randint

random_number = randint(1,20)
guess = 8
estimation = 0
name = input("Hi, what is your name? ")


print("Hello " + name + " !" + " I have chosen a number between 1 and 20\nYou have to guess it. You have 8 tries.")

while guess > 0:
    estimation = int(input("Enter your guess: "))
    guess = guess - 1

    if estimation < random_number:
        print("Your guess is lower than the number.")
    elif estimation > random_number:
        print("Your guess is higher than the number.")
    else:
        print(f"Congratulations {name}, you have guessed the number in {guess} tries.")
        break


if estimation != random_number:
    print(f"Sorry, you have run out of attempts. My number was {random_number}.")














