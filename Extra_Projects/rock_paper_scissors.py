import random

coor = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

def choice(): 
    c = input("Continue? (y/n):  ").lower()
    if c == 'y':
        player()
    elif c == 'n':
        quit()
    else:
        print("Please select (y/n)")
        choice()

def player():
    me = random.choice(['r', 'p', 's'])
    them = input("Rock, Paper, or Scissors? (r/p/s):  ").lower()
    while them not in ['r', 'p', 's']:
        print("Invalid choice.")
        them = input("Rock, Paper, or Scissors? (r/p/s):  ").lower()
    print("You chose", coor[them], "I chose", coor[me])

    if (me == 'r' and them == 'p') or \
       (me == 's' and them == 'r') or \
       (me == 'p' and them == 's'):
        print("You win!\n")
    elif (me == 'r' and them == 's') or \
         (me == 's' and them == 'p') or \
         (me == 'p' and them == 'r'):
        print("You lose.\n")
    else:
        print("Tie!\n")

    choice()

player()
