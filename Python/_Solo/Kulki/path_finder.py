import queue #https://docs.python.org/3/library/queue.html

start_i =0
start_j=0
end_i=0
end_j=0
board =[]
global iter
iter = 0




def find(location, in_board):
    global start_i
    global start_j
    global end_i
    global end_j
    global board
    global iter
    start_i = location[0][1]
    start_j = location[0][0]
    end_i = location[1][1]
    end_j = location[1][0]

    board = in_board

    nums = queue.Queue()
    nums.put("")
    add = ""
    path_find = True


    #Return path, for draw path on board in future
    while not findEnd(board, add):

        if nums.qsize() != 0:
            add = nums.get()

            for j in ["L", "R", "U", "D"]:
                put = add + j
                #print(put)
                if valid(board, put):
                    if len(put) < 3:
                        nums.put(put)
                    else:
                        if put[-1] == "L" and put[-2] != "R" or put[-1] == "R" and put[-2] != "L" or put[-1] == "U" and \
                                put[
                                    -2] != "D" or put[-1] == "D" and put[-2] != "U":
                            nums.put(put)
            if iter > 50000:
                print("to many iteration: ", iter)
                iter = 0
                path_find = False
                return path_find

        else:
            print("No Path ", iter)
            path_find = False
            printBoard(board, add)
            break


    return path_find
""" start_point(maze):

def start_point(maze):
    for x, pos in enumerate(maze[0]):
        if pos == 9:
            start = x


    return start
"""

def printBoard(board, path=""):


    i = start_i
    j = start_j
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(board):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(str(col) + " ", end="")
        print()


def valid(board, moves):
    path_pos = []

    i = start_i
    j = start_j
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if [i,j] in path_pos:
            return False


        if not (0 <= i < len(board[0]) and 0 <= j < len(board)):
            return False
        elif (board[j][i] == 1 or board[j][i] == 2 or board[j][i] == 3 or board[j][i] == 4 or board[j][i] == 5 or board[j][i] == 6 or board[j][i] == 7):
            return False
        path_pos.append([i, j])
    path_pos =[]
    return True


def findEnd(board, moves):

    global iter
    i = start_i
    j = start_j
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
    iter += 1
    if j == end_j and i == end_i:
        print("Found: " + moves + " No. of iteration: " + str(iter))
        #printMaze(board, moves)
        iter = 0
        return True

    return False



#for test:

"""
def createBoard():
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 7, 0],
             [0, 1, 0, 0, 0, 0, 0, 6, 0],
             [0, 1, 0, 0, 0, 0, 0, 5, 0],
             [0, 2, 7, 0, 7, 1, 1, 4, 0],
             [0, 4, 0, 0, 7, 0, 0, 0, 0],
             [0, 5, 0, 7, 7, 0, 2, 2, 1],
             [0, 7, 0, 0, 7, 0, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 7]]
    return board
#row, col 
locationtest = [[0,0],[8,0]]
Board = createBoard()
print(find(locationtest, Board))
"""



