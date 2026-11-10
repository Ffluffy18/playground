import random

computer_wins = 0

def computer_choice():
    # picks the computers choice
    computer = random.randint(1,3)
    if computer == 1:
        computer = 'rock'
        print(f'The computer picked {computer}')
    elif computer == 2:
        computer = 'paper'
        print(f'The computer picked {computer}')
    else:
        computer = 'scissors'
        print(f'The computer picked {computer}')
    return computer

def game(user, computer, player_wins=0):
    # gives you the outcome of a game
    if user == computer:
        print('Its a tie')
    elif user == 'rock' and computer == 'paper':
        print('You lose')
    elif user == 'paper' and computer == 'scissors':
        print('You lose')
    elif user == 'scissors' and computer == 'rock':
        print('You lose')
    else:
        player_wins += 1
        print('You win')
        return player_wins

    
print('Welcome to rock, paper, scissors game this will be a best out of 3')
    
while True:
    user = input('Choose either rock, paper, scissors: ').lower()

    if user == 'rock' or user == 'paper' or user == 'scissors':
        computer = computer_choice()
        game(user, computer)
        print(game(player_wins))
    elif user == 'q':
        break
    else:
        print("invalid input")
