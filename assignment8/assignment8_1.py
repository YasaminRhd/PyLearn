import random

options = [ 'Rock', 'Paper', 'Scissors']
scores = {'User': 0, 'Computer': 0}

for i in range(3):
    computer_choice = random.choice(options)
    user_chooice = input('Play the game: ').capitalize()
    
    if ((user_chooice == 'Rock' and computer_choice == 'Paper') 
        or (user_chooice == 'Paper' and computer_choice == 'Scissors') 
        or (user_chooice == 'Scissors' and computer_choice == 'Rock')):
        print('Computer wins!')
        scores['Computer'] += 1
                
    elif ((user_chooice == 'Rock' and computer_choice == 'Scissors') 
        or (user_chooice == 'Paper' and computer_choice == 'Rock') 
        or (user_chooice == 'Scissors' and computer_choice == 'Paper')):
        print('User wins!')
        scores['User'] += 1   
                 
    else:
        print('Draw!')
        
print(scores)