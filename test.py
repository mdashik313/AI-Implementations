from queue import PriorityQueue


dict = {}

dict['k'] = 2
s = 'as'
i = 5
dict['k'] = (s, i)

# print(dict['k'], type(dict['k'][0]), type(dict['k'][1]))

l = {}
li = [('d',5),('e',9)]
k = 'g'

# if k not in l :
#     l[k] = list()
# l[k].extend(li)
# print(l)

# if k not in l :
#     l[k] = int
# l[k]=2
# print(l)

# if ('e',9) not in l[k]:
#     l[k].extend([('e',9)])
# l[k].extend([('e',9)])
# l['s'] = []
# l['s'].extend([('a',29)])
# l['s'].extend([('d',23)])

# for node in l['s']:
#     print(node[1])

a = 16

# print(a** 0.5)

q = PriorityQueue()

# q.put((13,'a'))
# q.put((2,'c'))
# q.put((3,'d'))
# q.put((4,'e'))

# while not q.empty():
#     el = q.get()
#     print(el[0])


#class
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


pa = None
o = Node('a',pa,1,7)
q.put(o)
o = Node('d',o,2,5)
q.put(o)
# q.put(o)
# o = Node('c','a',3,4)
# q.put(o)
# o = Node('c','a',3,4)
# q.put(o)

temp = q.get()
# print(temp.key)
# temp = temp.parent
# print(temp.key)

while temp is not None:
    print(temp.key)
    temp = temp.parent

