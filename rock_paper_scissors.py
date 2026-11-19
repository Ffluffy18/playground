import random

max_key = 0
playerHistory = []
cw = 0
computer_payoff = 0
pw = 0
human_payoff = 0
ties = 0
rounds = 0

def computer_choice():
    # picks the computers choice
    computer = random.randint(1,3)
    if computer == 1:
        computer = 'rock'
    elif computer == 2:
        computer = 'paper'
    elif computer == 3:
        computer = 'scissors'
    return computer

def calculatePayoff(user, computer, con=0):
    # determines who wins or loses and returns users payoff
    if user == 'rock' and computer == 'paper':
        con = con - 1
        return con
    elif user == 'rock' and computer == 'scissors':
        con = con + 1
        return con
    elif user == 'paper' and computer == 'scissors':
        con = con - 1
        return con
    elif user == 'paper' and computer == 'rock':
        con = con + 1
        return con
    elif user == 'scissors' and computer == 'rock':
        con = con - 1
        return con
    elif user == 'scissors' and computer == 'paper':
        con = con + 1
        return con
    elif user == computer:
        con = 0
        return con

def analyzeStrategy(playerHistory):
    rock = playerHistory.count('rock')
    paper = playerHistory.count('paper')
    scissors = playerHistory.count('scissors')
    result_count = {'rock':rock, 'paper':paper, 'scissors':scissors}
    max_value = 0
    for key, value in result_count.items():
        if value >= max_value:
            max_value = value
            max_key = key
    return max_key

def computerStrategy(playerhistory, max_key):
    # pattern based computer strategy
    computer = random.randint(1, 9)
    if playerHistory == []:
        if computer <= 3:
            computer = 'rock'
        elif computer <= 6:
            computer = 'paper'
        elif computer <= 9:
            computer = 'scissors'
    elif max_key == 'rock':
        if computer <= 7:
            computer = 'paper'
        elif computer == 8:
            computer = 'scissors'
        elif computer == 9:
            computer = 'rock'
    elif max_key == 'paper':
        if computer <= 7:
            computer = 'scissors'
        elif computer == 8:
            computer = 'rock'
        elif computer == 9:
            computer = 'paper'
    elif max_key == 'scissors':
        if computer <= 7:
            computer = 'rock'
        elif computer == 8:
            computer = 'paper'
        elif computer == 9:
            computer = 'scissors'
    return computer

def displayResults():
    print(" ")
    print(f'Total Rounds {rounds}')
    print(" ")
    print(f'Human wins: {pw}')
    print(f'Computer wins: {cw}')
    print(f'Ties: {ties}')
    print(" ")
    print(f'Human total payoff: {human_payoff}')
    print(f'Computer total payoff: {computer_payoff}')
    print(" ")
    print(f'Human most common choice: {max_key}')
    print(" ")
    print(f'Computer Strategy: {choose_opponent}')


choose_opponent = int(input('Choose opponent 1 or opponent 2: (1 or 2) '))
# game loop
while True:
    # user and computer choices
    user = input("pick rock, paper, or scissors (q to quit): ").lower()
    if choose_opponent == 1:
        computer = computerStrategy(playerHistory, max_key)
        choose_opponent = 'pattern based'
    elif choose_opponent == 2:
        computer = computer_choice()
        choose_opponent = 'random'

    playerHistory.append(user)


    # player win or lose
    con = calculatePayoff(user, computer)
    if user == 'q':
        playerHistory.pop()
        break
    if con == -1:
        cw += 1
        human_payoff -= 1
        computer_payoff += 1
        rounds += 1
        print(f'The computer picked {computer} you lost')
    elif con == 1:
        human_payoff += 1
        computer_payoff -= 1
        pw += 1
        rounds += 1
        print(f'The computer picked {computer} you won')
    elif con == 0:
        ties += 1
        rounds += 1
        print(f'The computer picked {computer} its a tie')
    else:
        playerHistory.pop()
        print('Invalid Input')

    max_key = analyzeStrategy(playerHistory)

displayResults()

