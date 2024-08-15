import random
def play():
    user=input("What is your choice?'r' for rock,'p' for paper and 's' for scissors.")
    computer=random.choice(['r','p','s'])
    if user==computer:
        return "It is a tie"
    if win(user,computer):
        return "you won"
    return "you lost"
def win(player1,player2):
    if(player1=='r' and player2=='s')or (player1=='p' and player2=='r') or (player1=='s' and player2=='p'):
       return True
print(play())