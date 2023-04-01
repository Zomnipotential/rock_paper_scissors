'''
    The first working version. The simplest, yet complete, implementation.
    
    To Do:
    - Make a wrapper to check if the input is correct
    - Make it tolerable of changed number of options
    - Skip the while
    - Save the result for each separate session in a file, stamped with date and time
    - Every now and then bring up the stats and mock the user if you're ahead, or if you have won over the user before
    '''

import random

# Alternatives to choose from
options = ['Paper', 'Scissors', 'Rock']
def pick_winner(my_pick, user_pick):
    if user_pick == 2 and my_pick == 0:
        return 'I win'
    elif user_pick == 0 and my_pick == 2:
        return 'You win'
    else:
        if my_pick == user_pick:
            return 'nobody wins'
        if my_pick > user_pick:
            return 'I win'
        else:
            return 'You win'
        
print('To begin with, remember that: Rock wins over Scissors, which wins over Paper, which wins over Rock...')
print(f'{options[0]} (1),  {options[1]}(2),  {options[2]} (3)?')
print("R U Ready?\nLet's rock!")

while True:
    # computer makes its choice
    my_pick = random.randint(0,len(options)-1)
    
    # computer asks me to make a choice
    user_pick = int(input('... and you choose: '))-1
    
    # I do the rest and find out who is the winner
    print(f'You {options[user_pick]}, me {options[my_pick]}, {pick_winner(my_pick, user_pick)}')
