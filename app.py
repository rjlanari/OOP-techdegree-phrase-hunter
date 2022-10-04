from re import I
from phrasehunter.game import Game

if __name__ == '__main__':
    while True:
        game1 = Game()
        game1.start_game()
        if input('Do you want to play again? (Y/N) ').lower() not in ['y', 'yes']:
            print("\n")
            print("OK, see you next time!")
            print("\n")
            print("\n")
            break








