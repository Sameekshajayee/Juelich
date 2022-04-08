          #Excericse Day 1 : Fun with programming

#1. Lucky number 7
import random
from random import randint
choice = randint(1,10)
print(f'Random number is {choice}')
#a. If the random number is 7, print "lucky"
if(choice==7):
    print("lucky")
#b. Otherwise print "unlucky"
else :
    print("unclucky")


#2. Der Tuersteher
#a. Ask for age
age=(int(input('How old are you?')))

#b. Check if age is bigger or equal to 16 and below 18. If true print "You can enter, but only drink beer!"
if(age>=16 and age<18):
    print("You can enter, but only drink beer.")
#c. age bigger or equal to 18. Print "Have Fun!"
elif(age>=18):
    print("Have Fun!")
#d. Otherwise "You can not enter!"
else :
    print("You can not enter!")



#3. Schere Stein Papier
#a. Print out "Schere...Stein...Papier"
print("Schere...Stein...Papier")

#b. Ask player 1 adn player 2 for input
Player1= input('Player 1, make your move:')
Player2= input('Player 2, make your move:')

#c. Print the Winner !
if(Player1=='Schere' and Player2=='Stein' or Player1=='Stein' and Player2=='Papier' or Player1=='Papier' and Player2=='Schere'):
    print("Player2 wins")
elif(Player1==Player2):
   print("Draw")
elif(Player1=='Schere' and Player2=='Papier' or Player1=='Stein' and Player2=='Schere' or Player1=='Papier' and Player2=='Stein' ):
    print("Player1 Wins")
else:
    print("Not a valid input")

#e. Play against computer
Player1= input('Player 1, make your move:')
Possiblechoice = ("Schere", "Stein", "Papier")
Player2= random.choice(Possiblechoice)
print(f'Computer chose {Player2}')

if(Player1=='Schere' and Player2=='Stein' or Player1=='Stein' and Player2=='Papier' or Player1=='Papier' and Player2=='Schere'):
    print("Player2 wins")
elif(Player1==Player2):
   print("Draw")
elif(Player1=='Schere' and Player2=='Papier' or Player1=='Stein' and Player2=='Schere' or Player1=='Papier' and Player2=='Stein' ):
    print("Player1 Wins")
else:
    print("Not a valid input")




#4. Clean up Code with functions
#a. Two variable that keep score

player_wins=0
computer_wins=0

def display_header():

    print(f'Score till now: '
          f'Player Score - {player_wins}'
          f' Computer Score- {computer_wins}')
    print("Schere...Stein...Papier...")

def computer_move():
    Possiblechoice = ("Schere", "Stein", "Papier")
    Computer = random.choice(Possiblechoice)
    print(f'Computer chose {Computer}')
    return Computer
def calculate_winner(Player1, Computer):
    if ( Player1 == 'Schere' and Computer == 'Stein' or Player1 == 'Stein' and Computer == 'Papier' or Player1 == 'Papier' and Computer == 'Schere'):
        global computer_wins
        computer_wins +=1
        print(f'Winner of this round is computer')
    elif (Player1 == Computer):
        print("Draw")
    elif ( Player1 == 'Schere' and Computer == 'Papier' or Player1 == 'Stein' and Computer == 'Schere' or Player1 == 'Papier' and Computer == 'Stein'):
        global player_wins
        player_wins +=1
        print(f'Winner of this round is the player')
    else:
        print("Not a valid input")


def start_game():
    winning_score= 3
    while player_wins < winning_score and computer_wins < winning_score:
        display_header()
        player = input('(Enter your choice:)')

        if player == 'quit' or player =='q':
            break
        computer = computer_move()

        calculate_winner(player, computer)
    if(player_wins> computer_wins):
        print("Final Winner Is Player!!!\U0001f600")
    else:
        print("FINAL Winner IS Computer!!!\U0001f600")

def display_winner():
    if player_wins ==3:
        print(f'The winner is Player')
    elif computer_wins ==3:
        print(f'The winner is Computer')

start_game()

# 5. Emoji

smiley = "\U0001f600"
# print(f'The smiley is {smiley}')
for i in range(0, 6):
  for j in range(0, i):
      print(smiley, end="")
  print()











