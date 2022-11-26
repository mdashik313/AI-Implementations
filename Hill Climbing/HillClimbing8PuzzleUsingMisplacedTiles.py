
# input format:
# 3 1 2 
# 6 4 5
# 0 7 8

# output format:
# Neighbor [[3, 1, 2], [0, 4, 5], [6, 7, 8]] h=2
# Neighbor [[0, 1, 2], [3, 4, 5], [6, 7, 8]] h=0
# Neighbor [[1, 0, 2], [3, 4, 5], [6, 7, 8]] h=2

# solution [[0, 1, 2], [3, 4, 5], [6, 7, 8]] h=0


import copy

f = open('in.txt', 'r').readlines()

board = []

for line in f :
    board.append([eval(i) for i in line.strip().split(' ')])
    # [eval(i) for i in line] converts chars to int of a list

def MisplacedTile(board):
    # Goal state:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # here 0 means blank

    count = 0
    val = 0
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j] != val):
                count+=1
            val+=1
    return count
    
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
        t = (temp1,MisplacedTile(temp1),row-1,col)
        h.append(t)

    if(row < len(board)-1):
        #down
        temp2[row][col] = temp2[row+1][col]
        temp2[row+1][col] = 0
        t = (temp2,MisplacedTile(temp2),row+1,col)
        h.append(t)
    
    if(col > 0):
        #left
        temp3[row][col] = temp3[row][col-1]
        temp3[row][col-1] = 0
        t = (temp3,MisplacedTile(temp3),row,col-1)
        h.append(t)

    if(col < len(board)-1):
        #right
        temp4[row][col] = temp4[row][col+1]
        temp4[row][col+1] = 0
        t = (temp4,MisplacedTile(temp4),row,col+1)
        h.append(t)
    
    h.sort(key = lambda x: x[1]) #sor the list by second value
    return h[0] #h[0][0] is board, h[0][1] is misplacedTile
                # h[0][2],h[0][3] = row,col

def HillClimbing(board,row,col):  #row,col is position of blank tile
    current = (board,MisplacedTile(board),row,col)
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
