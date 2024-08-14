import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=(input(f"Guess the number between 1 and {x}:"))
        if(guess<random_number):
            print("Guess again,too low")
        elif(guess>random_number):
            print("Guess again,too high")
    print(f"Congratulations!You have guessed the right number {random_number}")
guess(20)