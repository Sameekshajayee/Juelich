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

#c. Play against computer
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









