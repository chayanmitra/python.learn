#How do you code rock, paper, and scissors in Python 3 in 2022?

#options is a list with 
#all the members a choice 
#you make in the game
options=['rock','paper','scissors']
#rules is a dictionary 
#set in such a way such that 
#if the player selects some text 
#that is in key then the player is defeated
rules = {'rock':'scissors',
         'paper':'rock',
         'scissors':'paper'}
import random
player_choice = input('Choose b\w rock, paper, or scissors:\n')
computer_choice = random.choice(options)
print("COMPUTER'S CHOICE IS:",computer_choice )
# player_choice in rules means 
#'Is player_choice among the keys of rules?'
if player_choice in rules:
    #rules.get(player_choice) gives the value of the key
    if rules.get(player_choice)==computer_choice:
        print('You win!')
    elif player_choice==computer_choice:
        print('Draw')
    else:
        print('You lose!')
else:
    print('Invalid choice')
