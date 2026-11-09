import random

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

def game(user, computer):
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
        print('You win')

    
print('Welcome to rock, paper, scissors game this will be a best out of 3')
    
while True:
    user = input('Choose either rock, paper, scissors: ').lower()
    for u in ['rock', 'paper', 'scissors']:
        if user != u:
            print('invalid input')
            break
        else:
            computer = computer_choice()
            game(user, computer)
            
            retry = input('Would you like to play again: ')
            if retry == 'n' or retry == 'no':
                break
