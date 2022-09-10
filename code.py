import random 
import utility 
import os
import hangman



random_words = ["word", "india", "potato", "tomato", "pizza"]
max_life = 6

word = random.choice(random_words)
blank_word = '_'*len(word)


while True:
    os.system('cls')
    hangman.draw_logo()
    hangman.draw_hangman(max_life)
    utility.draw_blanks(blank_word)
    
    inp = input("Guess a letter:")
    if inp in word:
        blank_word,max_life = utility.fill_blanks(word, blank_word, inp, max_life)
        if blank_word == word:
            utility.game_over("You Won!")
            break
        else:
            continue
    else:
        max_life = max_life - 1
        if max_life == 0:
            utility.game_over("You lost.")
            break



