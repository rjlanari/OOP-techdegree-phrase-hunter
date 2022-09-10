
# Create your Phrase class logic here.

# Create the method display
# Create the method check_letter
# Create the method check_complete

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.guessed = False

    def display(phrase):
        disp_list = []
        char_list = list(phrase)
        for i in char_list:
            if i == ' ':
                disp_list.append(' ')
            else:
                disp_list.append('_')
        print(''.join(disp_list))

    def check_letter(self, input_letter):
        return input_letter == self.phrase

    def check_phrase(self, all_letters):
        return all_letters == self.phrase

#if __name__ == '__main__':
