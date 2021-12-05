import random

words = ["book", 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste']

# convert string to list
word = list(random.choice(words))
_word =list( "-" * len(word) )

# set up the number of guesses
healthPoint = len(word) + 2

# creating hangman
print("- " * len(word))
 
while healthPoint > 0:
    user_character = input("enter your desired letter: ")
            
    # check if entered letter is correct or not
    if user_character in word:
        for i in range(len(word)):
            # replace - with enetered letter
            if user_character == word[i]:
                _word[i] = word[i]
        # convert list to string
        print("".join(_word))
        
    else:
        healthPoint = healthPoint - 1
        if healthPoint == 0:
            print("Game over! :) ")
            break
        print("wrong guess, try again! ")
        print("You have", healthPoint, "chances left")
        
    if "-" not in _word:
        print("you woOoOon!")
        break
