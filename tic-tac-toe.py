#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    board[position] = mark
    return


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    print(board[1],"|", board[2] ,"|", board[3])
    print("---------")
    print(board[4] ,"|", board[5] ,"|", board[6])
    print("---------")
    print(board[7] ,"|", board[8] ,"|", board[9])
    return


# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    position = int(position)
    if position >= 1 and position <= 9:
        if board[position] == ' ':
            result = True
        else:
            result = False
    else:
        result = False
    return result

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    if board[1] == board[2] == board[3] == player:
        result = True
    elif board [4] == board[5] == board[6] == player:
        result = True
    elif board [7] == board[8] == board[9] == player:
        result = True
    elif board [1] == board[4] == board[7] == player:
        result = True
    elif board [2] == board[5] == board[8] == player:
        result = True
    elif board [3] == board[6] == board[9] == player:
        result = True
    elif board [1] == board[5] == board[9] == player:
        result = True
    elif board [3] == board[5] == board[7] == player:
        result = True
    else:
        result = False
    return result


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for mark in board.keys():
        if board[mark] == ' ':
            return False
    return True


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
def switchUser():
    global currentTurnPlayer
    if currentTurnPlayer == 'X':
        currentTurnPlayer = 'O'
    else:
        currentTurnPlayer == 'O'
        currentTurnPlayer = 'X'

def replay():
    board_keys = []
    
    for mark in board:
        board_keys.append(mark)

    restart = input("Do you want to play again? (Y/N): ")

    if restart == "Y" or restart == "y":
        for mark in board_keys:
            board[mark] = ' '
        mainGame()
    elif restart == "N" or restart == "n":
        print("Thank you for playing!")
    else:
        print("Wrong input! Please choose between 'Y' or 'N'only.")
        replay()

def mainGame():
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")

        try:
            validateMove(move)
        except ValueError:
            print("Only put integer in this space!")
            continue
        
        if validateMove(move):
            markBoard(move, currentTurnPlayer)
            printBoard()
            if checkWin(currentTurnPlayer):
                print(f"Congratulations, {currentTurnPlayer} is the winner!")
                break
            if checkFull():
                print("The game has ended in a tie.")
                break
            switchUser()
        else:
            print("Wrong input! Please try again.") 
mainGame()
replay()

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over

def replay():
    board_keys = []
    
    for mark in board:
        board_keys.append(mark)

    restart = input("Do you want to play again? (Y/N): ")

    if restart == "Y" or restart == "y":
        for mark in board_keys:
            board[mark] = ' '
        mainGame()
    elif restart == "N" or restart == "n":
        print("Thank you for playing!")
    else:
        print("Wrong input! Please choose between 'Y' or 'N'only.")
        replay()
   
replay()