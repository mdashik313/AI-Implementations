import copy

f = open('in.txt', 'r').readlines()

board = []
IndexOfGoalStates = {}

for line in f :
    board.append([eval(i) for i in line.strip().split(' ')])
    # [eval(i) for i in line] converts chars to int of a list

#generate indexes(i,j) for each value in board
val = 0
for i in range(0,len(board)):
    for j in range(0,len(board[i])):
        IndexOfGoalStates[val]=(i,j)
        val+=1

def ManhattenDist(board):
    sum=0
    val=0
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j]!=val and board[i][j]!=0):
                sum += abs(i - IndexOfGoalStates[board[i][j]][0])
                sum += abs(j - IndexOfGoalStates[board[i][j]][1])
            val+=1
    return sum
    
def LowestCostSuccessor(board,row,col):
    h = []
    temp1 = copy.deepcopy(board)    
    temp2 = copy.deepcopy(board)
    temp3 = copy.deepcopy(board)
    temp4 = copy.deepcopy(board)

    if(row > 0):
        #up
        temp1[row][col] = temp1[row-1][col]
        temp1[row-1][col] = 0
        t = (temp1,ManhattenDist(temp1),row-1,col)
        h.append(t)

    if(row < len(board)-1):
        #down
        temp2[row][col] = temp2[row+1][col]
        temp2[row+1][col] = 0
        t = (temp2,ManhattenDist(temp2),row+1,col)
        h.append(t)
    
    if(col > 0):
        #left
        temp3[row][col] = temp3[row][col-1]
        temp3[row][col-1] = 0
        t = (temp3,ManhattenDist(temp3),row,col-1)
        h.append(t)

    if(col < len(board)-1):
        #right
        temp4[row][col] = temp4[row][col+1]
        temp4[row][col+1] = 0
        t = (temp4,ManhattenDist(temp4),row,col+1)
        h.append(t)
    
    h.sort(key = lambda x: x[1]) #sor the list by second value..ascending order
    return h[0] #h[0][0] is board, h[0][1] is misplacedTile
                # h[0][2],h[0][3] = row,col

def HillClimbing(board,row,col):  #row,col is position of blank tile
    current = (board,ManhattenDist(board),row,col)
    if(current[1]==0):
        return current
    global itr 
    itr = 0

    while True:
        itr+=1
        successor = LowestCostSuccessor(current[0],current[2],current[3])
        print('Neighbour',successor[0],'h =',successor[1])

        if(successor[1]>current[1]):
            return current
        current = successor

#get index of blank space
for i in range(0,len(board)):
    for j in range(0,len(board[i])):
        if(board[i][j]==0):
            row = i
            col = j
            break

temp = copy.deepcopy(board)
soln = HillClimbing(temp,row,col)

print('\nsolution',soln[0], 'h =', soln[1])
