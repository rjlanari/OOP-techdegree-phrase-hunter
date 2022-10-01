import random
from re import X
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
        if self.active_phrase.check_complete(self.guesses) == True:
            print("Congratulations, you've guessed the hidden phrase!")
        else:
            print('You did not find out the phrase, you lost!')
                

    def start_game(self):
        game_running = True
        self.welcome() 
        self.active_phrase = Phrase(self.get_random_phrase()) 
        print(str(self.active_phrase))  #just checking if the method worked
        self.active_phrase.display('')
        while game_running:
            self.get_guess() #get a letter from user, giving tuple with guesses
            print((self.guesses)) 
            if self.active_phrase.check_letter(self.guesses):
                self.active_phrase.display(self.guesses)
                if self.active_phrase.check_complete(self.guesses):
                    game_running = False
                else: 
                    game_running = True 
            else:
                self.missed += 1
                if self.missed > 4:
                    game_running = False
        
        self.game_over()
            
if __name__ == '__main__':

    game1 = Game()
    game1.start_game()
    #random_phrase = Phrase(game1.get_random_phrase())
    #print(random_phrase)
    #random_phrase.display('d')
    #letters = game1.get_guess()
    #print(letters)
