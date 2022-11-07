# input format:

# 6      (num of nodes)
# S 6 0  node_name x y (coordinate)
# A 6 0
# B 1 0
# C 2 0
# D 1 0
# G 0 0
# 9      (num of adjnodes)
# S A 1  node1 node2 weight
# S C 2
# S D 4
# A B 2
# B A 2
# B G 1
# C S 2
# C G 4
# D G 4
# S      (start-state)
# G      (goal-state)


from queue import PriorityQueue


f = open('in.txt', 'r')

nodes = {}
adjlist = {}
heuristic = {}
cumulativeCost = {}
parentNode = {}


#input nodes:

n = int(f.readline()) #read number of nodes

for i in range(n): #traverse
    line = f.readline().strip().split(' ')  #strip() for removing newline
    list_of_int = []
    for item in line:
        if(item.isdigit()):
            list_of_int.append(int(item))
    nodes[line[0]] = list_of_int
    # access values
    # l = nodes[line[0]]
    # print(nodes[line[0]][0],nodes[line[0]][1])


# print nodes:
# for node in nodes:
#     print(node, end=' --> ')
#     print(nodes[node])



#input adjlist:

n = int(f.readline()) #read num of adjnodes

for i in range(n):
    line = f.readline().strip().split(' ')
    
    #adjlist format: S --> [(A,1),(C,2)]
    if line[0] not in adjlist:
        adjlist[line[0]]=[]

    if line[1] not in adjlist:
        adjlist[line[1]]=[]

    #if graph is undirected do-->
    # if (line[1],line[2]) not in adjlist[line[0]]:
    #     adjlist[line[0]].extend([(line[1],line[2])])
        
    # if (line[0],line[2]) not in adjlist[line[1]]:
    #     adjlist[line[1]].extend([(line[0],line[2])])

    #if directed graph
    if (line[1],line[2]) not in adjlist[line[0]]:
        adjlist[line[0]].extend([(line[1],line[2])])


# print adjlist
# for node in adjlist:
#     print(node, end=' --> ')
#     for tupl in adjlist[node]:
#         print(tupl,end=' ')
#     print()



#input start and goal

start = f.readline().strip()
goal = f.readline().strip()


def calcHeuristic():
    for key in nodes:
        heuristic[key] = ((nodes[key][0]-nodes[goal][0])**2+(nodes[key][1]-nodes[goal][1])**2)**0.5


class Node :
    def __init__(self, key, parent, g, f):
        self.key = key
        self.parent = parent
        self.g = g
        self.f = f
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.key==other.key and self.parent==other.parent \
             and self.f==other.f and self.g==other.g 

    
def AStarSearch():
    q = PriorityQueue()
    cumulativeCost[start] = 0
    node_tuple = (cumulativeCost[start]+heuristic[start],start)
    
    q.put(node_tuple)

    while not q.empty() :
        curr = q.get()
        print(curr)
        if curr[1]==goal :
            #print path and cost
            path = goal
            temp = goal
            while temp != start :
                path = parentNode[temp] + ' --> ' + path
                temp = parentNode[temp]
            print('path : ',path)
            print('cost : ',cumulativeCost[goal])
            return
        
        neighbours = adjlist[curr[1]] #get neighbours of current node
        for neighbour in neighbours :
            
            #update cumulative cost of neighbour
            if neighbour[0] not in cumulativeCost:
                cumulativeCost[neighbour[0]] = int
            cumulativeCost[neighbour[0]] = cumulativeCost[curr[1]] + int(neighbour[1])  # neighbour[0] = neighbour name, neighbour[1] = weight
            
            #track parent node
            parentNode[neighbour[0]] = curr[1]

            node_tuple = (cumulativeCost[neighbour[0]]+heuristic[neighbour[0]],neighbour[0])
            q.put(node_tuple)



calcHeuristic()
print(heuristic)
print(adjlist)
AStarSearch()

# while not q.empty() :
#     print(q.get())

