import random
print("number guessing game")
number = random.randint(1,9)
Chances = 0
print("Guess a number between 1 to 9 : ")


while Chances < 5:

        guess =  int(input("Enter your guess : "))

        if guess == number:
            print("congratulation You Won !!!")
            break

        elif guess < number:
            print("your guess was almost close,guess a number higher than,you can do it")

        else :
            print("your guess was too high,guess a number lower than it,you can do it")


        Chances += 1

        if not Chances < 5:
            print("You lost!!! The number is",number)
