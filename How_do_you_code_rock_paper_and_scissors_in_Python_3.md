# How do you code rock, paper, and scissors in Python 3 in 2022?

The .py file is [here in my github repository](https://github.com/chayanmitra/python.learn/blob/main/Rock%2C%20Paper%2C%20and%20Scissors.py)

### Options and rules are introduced as lists and dictionaries simultaneously

```
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
```

### player_choice takes the input from the player whereas, computer_choice takes a random input from the computer

```
player_choice = input('Choose rock, paper, or scissors:\n')
computer_choice = random.choice(options)
```
>Choose rock, paper, or scissors:
rock
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Input In [2], in <cell line: 2>()
      1 player_choice = input('Choose rock, paper, or scissors:\n')
----> 2 computer_choice = random.choice(options)

NameError: name 'random' is not defined

### Since, the program did not recognize random.choice() hence, we introduce random module

```
import random
player_choice = input('Choose rock, paper, or scissors:\n')
computer_choice = random.choice(options)
```

### Now we use the conditional statement to decide the winner

```
# player_choice in rules means 
#'Is player_choice among the keys of rules?'
if player_choice in rules:
    #rules.get(player_choice) gives the value of the key
    if rules.get(player_choice)==computer_choice:
        print('You win!')
    else:
        print('You lose!')
else:
    print('Invalid choice')
```

### The Whole Program is written below

```
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
```

# Now download this program from the repository and Play! 😉
