import random
import hangman_StagesAndList
print("Let's play Hangman game!")
lives=6
chosen_word=random.choice(hangman_StagesAndList.word)
display=[]
for i in chosen_word:
    display.append("_")
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if letter==guessed_letter:
            display[i]=guessed_letter
    print(display) 
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You loose!")
    print(hangman_StagesAndList.stages[lives])
    if '_' not in display:
        game_over=True
        print("You win!")
    
    
            
            
