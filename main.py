#Step 1 
import random
import hangman_words
import hangman_art

stages=hangman_art.stages
logo=hangman_art.logo
word_list=hangman_words.word_list
chosen_word=random.choice(word_list)

print(f'chose word is : {chosen_word}')
word_length=len(chosen_word)
lives=6
end_of_game=False


print(logo)

display=[]
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
        print(f'" {user_guess} " is not in the word. You lose a life.')
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