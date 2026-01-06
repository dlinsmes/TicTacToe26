
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

    #need to cast string input to int
    moveRow = int(input("enter your row:"))
    moveCol = int(input("enter your col:"))

    while moveRow < 0 or moveRow >= size or moveCol < 0 or moveCol >= size or board[moveRow][moveCol] != "_":
        print("invalid")
        moveRow = int(input("enter your row:"))
        moveCol = int(input("enter your col:"))

    board[moveRow][moveCol] = piece

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