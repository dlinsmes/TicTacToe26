# global variables - same as class variables
# - can be used in any function in the file

#no data types when declaring variables
size = 3

#list - starts as empty, then add values
board = []
piece = "o"
moveRow = -1
moveCol = -1


#defines a function
def main():
    print("welcome to tic tac toe")
    setupBoard()
    printBoard()

    while not winner() and not tie():
        changePiece()
        makeMove()
        printBoard()

    if winner():
        print(piece + " won!")
    else:
        print("tie")

def winner():

    rowCount = 0
    colCount = 0
    d1Count = 0
    d2Count = 0

    for i in range(size):
        if board[moveRow][i] == piece:
            rowCount += 1
        if board[i][moveCol] == piece:
            colCount += 1
        if board[i][i] == piece:
            d1Count += 1
        if board[size-i-1][i] == piece:
            d2Count += 1

    if rowCount == size or colCount == size or d1Count == size or d2Count == size:
        return True

    return False

def tie():
    for row in board:
        for spot in row:
            if spot == "_":
                return False
    return True

def changePiece():
    #sometimes when you want to use a global variable
    #you need to re-reference it with this line
    global piece

    if piece == "o":
        piece = "x"
    else:
        piece = "o"

def makeMove():
    global moveRow
    global moveCol

    print(piece +"'s turn")


    if piece == "o":
        moveRow, moveCol = computerMove()

    else:

        #need to cast string input to int
        moveRow = int(input("enter your row:"))
        moveCol = int(input("enter your col:"))

        while moveRow < 0 or moveRow >= size or moveCol < 0 or moveCol >= size or board[moveRow][moveCol] != "_":
            print("invalid")
            moveRow = int(input("enter your row:"))
            moveCol = int(input("enter your col:"))

    board[moveRow][moveCol] = piece

def computerMove():

    #need to use the existing winner() and tie() functions that each use
    # these global variables
    global moveRow
    global moveCol
    global piece

    row = -1
    col = -1

    #loop through the board
    #simulate placing the program's piece and evaluating the score
    #of that placement
    #-after finding the score of each placement, pick the move with the
    #best score

    hiScore = -2
    for i in range(size):
        for j in range(size):
            if board[i][j] == "_":
                piece = "o"
                moveRow = i
                moveCol = j
                board[i][j] = piece
                score = evaluate("program")

                #undo the move so that we can check the score of
                #the next placement
                board[i][j] = "_"
                if score > hiScore:
                    hiScore = score
                    row = i
                    col = j

    #evaluate() might simulate multiple following turns and alternate the piece
    piece = "o"
    #return the row and col where the hi score was found
    return row, col

#determine the score of player after they simulate placing their piece
def evaluate(player):
    global moveRow
    global moveCol
    global piece

    #score of 1 means the prev program move ended the game with a win
    if player == "program" and winner():
        return 1
    #score of -1 means that the program lost bc the other player just won
    elif player == "other" and winner():
        return -1
    elif tie():
        return 0

    #the move made didn't end the game and there are still more moves
    #to simulate to continue the game

    # if the program just took their turn, need to simulate the
    # other player going next
    if player == "program":
        #same steps as the computerMove function, but now simulate the
        #other player making a follow-up move
        bestScore = 2
        for i in range(size):
            for j in range(size):
                if board[i][j] == "_":
                    piece = "x"
                    moveRow = i
                    moveCol = j
                    board[i][j] = piece
                    score = evaluate("other")
                    board[i][j] = "_"
                    if score < bestScore:
                        bestScore = score
        return bestScore

    else:
        #we just simulated the other player taking a turn, but that didn't
#lead to a game over situation
#-need to simulate the program going again
        bestScore = -2
        for i in range(size):
            for j in range(size):
                if board[i][j] == "_":
                    piece = "o"
                    moveRow = i
                    moveCol = j
                    board[i][j] = piece
                    score = evaluate("program")
                    board[i][j] = "_"
                    if score > bestScore:
                        bestScore = score
        return bestScore


def setupBoard():
    #i iterates 0-1-2
    for i in range(size):
        row = []
        for j in range(size):
            row.append("_")
        board.append(row)

def printBoard():
    #for each loop
    for row in board:
        # print(row)
        #append all the pieces to a string to print
        line = ""
        for spot in row:
            line += spot + " "
        print(line)

#need to explicitly call main() to run it
#after it's defined
main()