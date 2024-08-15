import random
def guess(z):
    low=1
    high=z
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=high
        feedback=input(f'is {guess} too high(H), too low(L) or correct(C)?').lower()
        if feedback=='h':
           high= guess-1
        elif feedback=='l':
           low= guess+1
    print("Congratulations!The computer guessed your number correctly! ")
guess(30)