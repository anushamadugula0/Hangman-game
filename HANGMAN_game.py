import random
#import hangman_stages
stages= ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
 '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
+---+
  |   |
      |
      |
      |
      |
=========''']
print("Let's play Hangman game!")
lives=6
word=['apple','beautiful','potato','ugly','good','love','anusha','venkat','bobby','chandu','lokesh','vasu','priya','nandu','suharika','satya','hema','sai','devi']
chosen_word=random.choice(word)
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
    #print(hangman_stages.stages[lives])
    print(stages[lives])
    if '_' not in display:
        game_over=True
        print("You win!")
    
    
            
            
