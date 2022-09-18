# Create your Phrase class logic here.

# Create the method display
    #make a list of characters that are in the phrase
    #if the character is ' '
    #append ' ' to the resulting list
    #else for every character in the prhase.list
    #append '_' to the resulting list
    #return joint resulting list

# Create the method check_letter 
    #make a list of the characters in the phrase
    #takes the imput letter
    #returns true if the imput letter is in the litst of letters

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
        return input_letter == self.phrase
        
    def check_phrase(self, all_letters):
        return all_letters == self.phrase
    
if __name__ == '__main__': 
    
    phrase1 = Phrase('hola mundo')
    print(phrase1)
    phrase1.display('o', 'l', 'a')