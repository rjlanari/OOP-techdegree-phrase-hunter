# Create your Phrase class logic here.

# Create the method check_complete
    #make a list of the characters in the phrase
    #get a list of letters that the player gessed
    #return true when the all the gessed letters are in the list frase

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.guessed = False

    def __str__(self):
        return f'{self.phrase}'

    
    def display(self, *guessed_letters):
        disp_list = []
        for i in self.phrase:
            if i == ' ':
                disp_list.append(' ')         
            else:    
                disp_list.append('_')
        for x in guessed_letters:
            for ind in list((index for index, elem in enumerate(self.phrase) if elem == x)):
                disp_list[ind] = x
    
        print(''.join(disp_list)) 
        
    def check_letter(self, input_letter):
        return input_letter in self.phrase
        
    def check_complete(self, *guessed_letters):
        if set(self.phrase) - {' '} == set(guessed_letters): #eliminates blank spaces from phrase
            return True
        else:
            return False
    
if __name__ == '__main__': 
    
    phrase1 = Phrase('hola manola')
    print(phrase1)
    phrase1.display()
    print(phrase1.check_letter('r'))
    print(phrase1.check_complete('h','o','l','a','m','u','n','d'))
    