import random

pw = 0 # player wins
cw = 0 # computer wins

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

def game(user, computer, con=0):
    '''determines who wins or loses'''
    if user == 'rock' and computer == 'paper':
        con = con + 2
        return con
    elif user == 'rock' and computer == 'scissors':
        con = con + 1
        return con
    elif user == 'paper' and computer == 'scissors':
        con = con + 2
        return con
    elif user == 'paper' and computer == 'rock':
        con = con + 1
        return con
    elif user == 'scissors' and computer == 'rock':
        con = con + 2
        return con
    elif user == 'scissors' and computer == 'paper':
        con = con + 1
        return con

def wins(pw, cw):
    ''' returns output saying outcome of the match'''
    if pw == 1 and pw > cw:
        print('you win')
    elif cw == 1 and pw < cw:
        print('you lose')
    elif pw == 2 and pw > cw:
        print('you won it all')
    elif cw == 2 and pw < cw:
        print('you lost it all')
    elif cw == pw:
        print('you are tied')

while pw < 2 and cw < 2:
    user = input('Choose either rock, paper, scissors: ').lower()
    computer = computer_choice()
    if user == computer:
        print(f'this is a tie, the score is {pw}:{cw}')
    else:
        con = game(user, computer)

        if con == 1:
            pw += 1
        elif con == 2:
            cw += 1
        wins(pw, cw)

print('GG')
