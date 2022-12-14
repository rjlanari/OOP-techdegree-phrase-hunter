from curses.ascii import isalpha
import random
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
                        Phrase("if you stay ready you aint got to get ready"),
                        Phrase("all tea all shade"),
                        Phrase("she already done had herses"),
                        Phrase("to be able to blend that is what realness is"),
                        Phrase("the shoulders should match them hips but they dont")
                        ]
        self.active_phrase = None
        self.guesses = [] #list of letter provided by user
        
    def get_random_phrase(self):    
        self.active_phrase = random.choice(self.phrases)
        return self.active_phrase
    
    def welcome(self):
        print("Hello, welcome to the Phrase Guessing Game!")
    
    def get_guess(self):
        while True:
            try:
                guess = input('Please, enter a letter that you think would be in the phrase! ').lower()
                print("\n")
                if not isalpha(guess):
                    print('That is not a valid letter!')
                    print("\n")   
                else:
                    break
            except TypeError:
                print('That is not a valid letter! Please, chose one letter!')
                print("\n")    
         
            continue

        self.guesses.append(guess)
        return self.guesses

        
    
    def game_over(self):
        if self.active_phrase.check_complete(self.guesses) == True:
            print("Congratulations, you've guessed the hidden phrase!")
            print("\n")
        else:
            print('You did not find out the phrase, you lost!')
            print("\n")
                

    def start_game(self):
        game_running = True
        print("\n")
        self.welcome()
        self.active_phrase = Phrase(self.get_random_phrase())
        self.active_phrase.display('')
        while game_running:
            self.get_guess()
            if self.active_phrase.check_letter(self.guesses):
                self.active_phrase.display(self.guesses)
                if self.active_phrase.check_complete(self.guesses):
                    game_running = False
                else: 
                    game_running = True 
            else:
                self.missed += 1
                print(f'You have {5-self.missed} out of 5 lives remaining!')
                print("\n")
                if self.missed > 4:
                    game_running = False

        self.game_over()

    