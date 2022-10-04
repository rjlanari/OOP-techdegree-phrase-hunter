from sqlite3 import enable_shared_cache


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.guessed = False

    def __str__(self):
        return f'{self.phrase}'

    
    def display(self, guessed_letters):
        for i in str(self.phrase):
            if i == ' ' or i in guessed_letters:
                print(i, end='')
            else: 
                print('_', end='')
        print("\n")    

    def check_letter(self, guessed_letters):
        return str(guessed_letters[len(guessed_letters)-1]) in str(self.phrase)


    def check_complete(self, guessed_letters):
        if set(str(self.phrase)) - {' '} == set((guessed_letters)): #eliminates blank spaces from phrase
            return True
        else:
            return False
    
if __name__ == '__main__': 
    
    phrase1 = Phrase('hola manola')
    print(phrase1)
    print(list(str(phrase1)))
    guessed = ['a', 'h', 'n']
    phrase1.display(guessed) #when I pass a tuple the method does not work
    #phrase1.display('a', 'h')
    print(phrase1.check_letter(['o','p','l']))
    print(phrase1.check_complete(['h','o','l','a','n','m']))
    