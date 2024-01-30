#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)

display=[]
for letter in chosen_word:
    display+= "_"

print(display)
user_guess=input("Guess a letter:").lower()
#assign correct user guess and display it
for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==user_guess:
        display[position]=letter
print(display)
#check if user guess letter is in the chosen word
for letter in chosen_word:
    if user_guess == letter:
        print("Right")
    else:
        print("Wrong") 
