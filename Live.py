import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome():
    name = input('What is your name? [Only letters allowed in username and no spaces] ')

    try:
        if any([i > 'z' or i < 'a' for i in name]):
            print("Error. Contains illegal characters")
            welcome()
        elif name == '' or name == ' ':
            print('Error. No blanks')
            welcome()
        elif len(name) > 15:
            print('Error. Username too long')
            welcome()
        else:
            print(f'Welcome {name}, to the World of Games (WoG).'
                  f' Here you can play many cool games')
            pass

    except ValueError:
        print('invalid')


def load_game():
    game1 = 'The Memory Game'
    game2 = 'The Guessing Game'
    game3 = 'The Currency Roulette Game'

    while True:
        try:
            g = int(input('What game would you like to play? [1/2/3] '))

            if int(g) == 1:
                print(f'{game1}: A sequence of numbers will appear for 1 second, and you have'
                      f' to guess it back.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                MemoryGame.play(difficulty)

            if int(g) == 2:
                print(f'{game2}: Guess a number and see if you chose'
                      f' like the computer.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                GuessGame.play(difficulty)

            if int(g) == 3:
                print(f'{game3}: Try and guess the value of a random'
                      f' amount of USD in ILS.')
                difficulty = int(input('What difficulty would you like to play? [1/2/3/4/5] '))
                CurrencyRouletteGame.play()

        except ValueError:
            print('Invalid input. You can only enter numbers')

#
#
#
#
#
#         # difficulty = int()
#         # if difficulty == 1:
#         #     print('Very Easy')
#         # elif difficulty == 2:
#         #     print('Easy')
#         # elif difficulty == 3:
#         #     print('Medium')
#         # elif difficulty == 4:
#         #     print('Hard')
#         # elif difficulty == 5:
#         #     print('Very Hard')
#         # else:
#         #     print("Invalid input. Your only options are 1-5. let's start over")
#         #     load_game()
