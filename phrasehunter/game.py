
import random
from phrase import Phrase

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
        self.guesses.append(guess)
        return self.guesses
    
    def game_over(self):
        if self.missed > 4 and Phrase.check_phrase(self.guesses) == False:
            print("You haven't guessed the hidden phrase, the game is over!")
        elif Phrase.check_phrase(self.guesses) == True:
            print("Congratulations, you've guessed the hidden phrase!")

    def start_game(self):
        game_running = True
        self.welcome()
        self.active_phrase = Phrase(self.get_random_phrase())
        self.active_phrase.display()
        guessed = tuple(self.get_guess())
        print(guessed)
        self.active_phrase.display(guessed)
        
            

    


if __name__ == '__main__':

    game1 = Game()
    #random_phrase = Phrase(game1.get_random_phrase())
    #print(random_phrase)
    #random_phrase.display('d')
    game1.start_game()
    #letters = game1.get_guess()
    #print(letters)
    
