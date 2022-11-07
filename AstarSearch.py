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

# ans
# path :  S --> C --> G
# cost :  6

# test case:
# 5
# S 1 2
# A 2 2
# C 1 1
# D 2 2
# G 4 5
# 7
# S A 7
# A G 1
# S G 10
# C A 2
# D G 1
# S C 1
# S D 1
# S
# G
# path :  S --> D --> G
# cost :  2


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
    def __str__(self):
        return f"{self.key} {self.parent} {self.g} {self.f}"
    
def AStarSearch():
    q = PriorityQueue()
    start_node = Node(start,None,0,heuristic[start])
    q.put(start_node)

    while not q.empty() :
        curr = q.get()
        if curr.key==goal :
            #print path and cost
            cost = curr.g
            path = goal
            temp = curr.parent
            while temp is not None :
                path = temp.key + ' --> ' + path
                temp = temp.parent
            print('path : ',path)
            print('cost : ',cost)
            return
        
        neighbours = adjlist[curr.key] #get neighbours of current node
        for neighbour in neighbours :
            neighbourNode = Node(neighbour[0],curr,curr.g+int(neighbour[1]),curr.g+int(neighbour[1])+heuristic[neighbour[0]])            
           
            q.put(neighbourNode)



calcHeuristic()
AStarSearch()

