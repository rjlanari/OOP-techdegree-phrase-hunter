
import random
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
                        "a bird in the hand is worth two in the bush",
                        "an apple a day keeps the doctor away",
                        "it takes two to tango",
                        "like taking candy from a baby",
                        "you can not make an omelet without breaking some eggs"
                        ]
        self.active_phrase = None
        self.guesses = [] #list of letter provided by user
        
    def get_random_phrase(self):    
        self.active_phrase = random.choice(self.phrases)
        return self.active_phrase
    
    def welcome(self):
        print("Hello, welcome to the Phrase Guessing Game!")
    
    def get_guess(self):
        guess = input('Please, enter a letter that you think would be in the phrase!')      
        self.guesses.append(guess.lower())
        return self.guesses
    
    def game_over(self):
        if self.missed > 4 and Phrase.check_complete(self.guesses) == False:
            print("You haven't guessed the hidden phrase, the game is over!")
            game_running = False
        elif Phrase.check_complete(self.guesses) == True:
            print("Congratulations, you've guessed the hidden phrase!")
            game_running = False
        else: 
            game_running = True
        

    def start_game(self):
        game_running = True
        self.welcome() 
        self.active_phrase = Phrase(self.get_random_phrase()) 
        self.active_phrase.display()
        while game_running:
            guessed = str(self.get_guess()) #get a letter from user, giving tuple with guesses
            if self.active_phrase.check_letter(guessed):#if letter in the frease
                self.active_phrase.display(tuple(guessed))#display the frase with that letter
                self.game_over()
            else:
                self.missed =+ 1
                self.game_over() #check if the game is over
            

