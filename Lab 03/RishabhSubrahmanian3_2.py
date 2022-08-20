import random


def rps():
    print('----------------------')
    print('Rock - Paper - Scissors')
    print('----------------------')

    response = input('Enter response: ').lower().strip()
    while response not in ['rock', 'paper', 'scissors']:
        response = input('Enter valid response: ').lower().strip()

    return response


def main():

    win = 0
    lose = 0
    tie = 0
    game_number = 0
    while True:
        your_choice = rps()
        comp_choice = random.choice(['rock', 'paper', 'scissors'])
        if comp_choice == 'rock':
            if your_choice == 'rock':
                tie += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You tie.')
            elif your_choice == 'paper':
                win += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You win.')
            elif your_choice == 'scissors':
                lose += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You lose.')
            game_number += 1
        elif comp_choice == 'paper':
            if your_choice == 'rock':
                lose += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You lose.')
            elif your_choice == 'paper':
                tie += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You tie.')
            elif your_choice == 'scissors':
                win += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You win.')
            game_number += 1
        else:
            if your_choice == 'rock':
                win += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You win.')
            elif your_choice == 'paper':
                lose += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You lose.')
            elif your_choice == 'scissors':
                tie += 1
                print(f'Computer is {comp_choice}. You are {your_choice}. You tie.')
            game_number += 1

        if game_number == 3:
            break

    if win == lose:
        print('GAME OVER - YOU TIE')
    elif win > lose:
        print('GAME OVER - YOU WIN')
    else:
        print('GAME OVER - COMPUTER WINS')


if __name__ == '__main__':
    main()
