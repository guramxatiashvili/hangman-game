#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)
print(f'chose word is : {chosen_word}')
display=[]

word_length=len(chosen_word)
for letter in chosen_word:
    display+= "_"

print(display)

end_of_game=False
while not end_of_game:
    user_guess=input("Guess a letter:").lower()
    #assign correct user guess and display it
    for position in range(word_length):
        letter=chosen_word[position] 
        if letter==user_guess:
            display[position]=letter
    #if no '_' in display, then end of game        
    if '_' not in display:
        end_of_game=True
        print("You win!")
    print(display)

# for letter in chosen_word:
#     if user_guess == letter:
#         print("Right")
#     else:
#         print("Wrong") 
