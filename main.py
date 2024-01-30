#Step 1 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)

print(f'chose word is : {chosen_word}')
display=[]
word_length=len(chosen_word)
lives=6
end_of_game=False


for letter in chosen_word:
    display+= "_"

print(display)

while not end_of_game:
    user_guess=input("Guess a letter:").lower()
    #assign correct user guess and display it
    for position in range(word_length):
        letter=chosen_word[position] 

        if letter==user_guess:
            display[position]=letter

    if user_guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lost!")
        print(f'You have {lives} lives left')
    #if no '_' in display, then end of game        
    if '_' not in display:
        end_of_game=True
        print("You win!")
    print(display)
    print(stages[lives]) #show ascii character position based on remaning lives