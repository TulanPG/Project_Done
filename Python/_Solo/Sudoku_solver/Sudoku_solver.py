# based on http://taborsudoku.pl/sudoku-start/
# https://pl.qwe.wiki/wiki/Sudoku_solving_algorithms
# ITS BACKTRACKING type of algorithm
board1 = [
    [0, 8, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 9, 2, 0],
    [0, 0, 0, 0, 4, 0, 5, 0, 3],

    [0, 7, 0, 0, 0, 2, 0, 1, 0],
    [0, 0, 0, 0, 0, 3, 0, 9, 0],
    [0, 2, 8, 0, 0, 7, 0, 0, 0],

    [2, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 4],
    [3, 0, 0, 1, 0, 0, 0, 0, 7]
]

board = [
    [1, 0, 0, 0, 7, 0, 0, 3, 0],
    [8, 3, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 2, 9, 0, 0, 6, 0, 8],

    [0, 0, 0, 0, 0, 4, 9, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 4],

    [2, 0, 3, 0, 0, 9, 1, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 4, 3],
    [0, 4, 0, 0, 8, 0, 0, 0, 9]
]

def draw_board(table):
    for x in range(9):
        if x == 0:
            print()
            print("Sudoku Board in Console:")
            print()
            print("Pos Y  0 1 2  | 3 4 5  | 6 7 8 ")
            print("X------------------------------")

        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - - - - ")

        for y in range(9):
            if y % 3 == 0:
                if y != 0:
                    print(" | ", end="")
                else:
                    print(x, "  |  ", end="")

            if y == 8:
                print(table[x][y])
            else:
                print(str(table[x][y]) + " ", end="")

    print("-------------------------------")


def where_empty(table):
    # return first in row zeros position
    for x in range(9):
        for y in range(9):

            if table[x][y] == 0:
                pos = x, y
                return pos
    return None


def solver(table):

    # print(where_empty(table))
    if where_empty(table) is None:
        return True
    else:
        pos = where_empty(table)

    # check solution
    for i in range(1, 10):
        if is_valid(table, pos, i):
            table[pos[0]][pos[1]] = i

            if solver(table):
                return True

            table[pos[0]][pos[1]] = 0
    return False


def is_valid(table, pos, num):
    # Row
    for x in range(9):
        # Check in every row, except pos[1] is "num" in row
        if table[pos[0]][x] == num and pos[1] != x:
            return False
    # Col
    for x in range(9):
        # Check in every row, except pos[1] is "num" in row
        if table[x][pos[1]] == num and pos[0] != x:
            return False

    # boxes
    x_box = int(pos[0] / 3)
    y_box = int(pos[1] / 3)

    for x in range(x_box * 3, ((x_box + 1) * 3)):
        for y in range(y_box * 3, ((y_box + 1) * 3)):

            if table[x][y] == num and table[pos[0]][pos[1]] != num:  # sprawdzić czy dodać "and"
                return False
    return True


def writte_board(board):
    #Give table + solved to txt
    filepath = "boards.txt"
    f = open(filepath,"a") # w - writte, a - append
    f.write((str(board)+"\n"))
    f.close()

def board_from_txt(number_of_sudoku):
    filepath = "boards.txt"
    f = open(filepath, "r")
    bb =[]
    board=[]
    count = 0
    readline = f.readlines()[number_of_sudoku]
    b = list(readline.replace(" ","").replace("[","").replace("]","").split(","))
    print(b)
    f.close()
    for y in range(0,9):
        for x in range (0,9):
            bb.append(int(b[count]))
            count +=1
        board.append(bb)
        bb=[]

    return board

#Writte and read file with sudoku table
#writte_board(board1) # you can add next board there
b = board_from_txt(0)  # for now its (0, 1)
draw_board(b)
solver(b)
draw_board(b)

#Casual solver of sudoku
#draw_board(board)
#solver(board)
#draw_board(board)



#draw_board(board)
#solver(board)
#draw_board(board)
