f = open('in.txt', 'r')

nodes = {

}
num_nodes = int(f.readline()) #read number of nodes
for i in range(0,num_nodes): #traverse
    line = f.readline()
    line = line.strip() #remove newline
    line = line.split(' ')
    list_of_int = []
    for item in line:
        if(item.isdigit()):
            list_of_int.append(int(item))
    print(list_of_int)