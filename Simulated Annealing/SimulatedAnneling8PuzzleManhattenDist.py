
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
import math
import random

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

def schedule(t):
    if t > 300 : return 0
    return 300 - t
    
def RandomSuccessor(board,row,col):
    availableMoves = []
    temp1 = copy.deepcopy(board)    
    temp2 = copy.deepcopy(board)
    temp3 = copy.deepcopy(board)
    temp4 = copy.deepcopy(board)

    if(row > 0):
        availableMoves.append('U')
        #up
    if(row < len(board)-1):
        availableMoves.append('D')
        #down
    if(col > 0):
        availableMoves.append('L')
        #left
    if(col < len(board)-1):
        availableMoves.append('R')
        #right
    
    random_move = random.choice(availableMoves)

    match random_move:
        case 'U':
            temp1[row][col] = temp1[row-1][col]
            temp1[row-1][col] = 0
            t = (temp1,ManhattenDist(temp1),row-1,col)
        case 'D':
            temp2[row][col] = temp2[row+1][col]
            temp2[row+1][col] = 0
            t = (temp2,ManhattenDist(temp2),row+1,col)
        case 'L':
            temp3[row][col] = temp3[row][col-1]
            temp3[row][col-1] = 0
            t = (temp3,ManhattenDist(temp3),row,col-1)
        case 'R':
            temp4[row][col] = temp4[row][col+1]
            temp4[row][col+1] = 0
            t = (temp4,ManhattenDist(temp4),row,col+1)

    return t


def HillClimbing(board,row,col):  #row,col is position of blank tile
    
    current = (board,ManhattenDist(board),row,col)
    global itr
    itr = 0

    for t in range(1,301):
        T = schedule(t)
        if(T==0 or current[1]==0):
            return current
        
        successor = RandomSuccessor(current[0],current[2],current[3])
        print('Neighbour',successor[0],'h =',successor[1])
        del_E = current[1] - successor[1]

        if(del_E >= 0):
            current = successor
        else:
            p = math.exp(del_E/T)
            if(random.random() <= p):
                current = successor

        itr += 1

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
