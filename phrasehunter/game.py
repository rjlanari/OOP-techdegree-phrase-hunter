# Create your Game class logic in here.
    #make class Name
    #define __init__ 
        #missed
        #phrases
        #active_phrase none

import random
from phrase import Phrase
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
                        "A bird in the hand is worth two in the bush",
                        "An apple a day keeps the doctor away",
                        "It takes two to tango",
                        "Like taking candy from a baby",
                        "You can't make an omelet without breaking some eggs"
                        ]
        self.active_phrases = None
        self.guesses = []
    
    # getting a random phrase,     
    def get_random_phrase(self):    
        random_phrase = random.choice(self.phrases)
        return random_phrase
    
    def welcome(self):
        print("Hello, welcome to the Phrase Guessing Game!")
    
    def get_guess(self):
        self.guesses = input('Please, enter a letter that you think would be in the phrase!')
        return self.guesses
    
  
    # handling interactions, 

    # checking for a win/loss state, 
    
    # adding to the number missed.
    
    # def game_over(self):
        #if missed > 5 print Game over
        #end game
    # Start method
