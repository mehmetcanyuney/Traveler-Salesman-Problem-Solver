def greedy_algorithm(nodes):
    solution = []
    free_nodes = nodes[:]
    n = free_nodes[0]
    free_nodes.remove(n)
    solution.append(n)
    total_travel = 0
    while len(free_nodes) > 0:
        min_lenght = None
        min_node = None
        for i in free_nodes:
            lenght = n.distance(i)
            if min_lenght is None:
                min_lenght = lenght
                min_node = i
            elif lenght < min_lenght:
                min_lenght = lenght
                min_node = i
        total_travel += min_lenght
        solution.append(min_node)
        free_nodes.remove(min_node)
        n = min_node
    return solution,total_travel


class Node:
    # initiliazing
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    # basic writing function for testing
    def classp(self):
        print(self.id, end=" ")
        print(self.x, end=" ")
        print(self.y, end=" ")
        print()

    # calculating distance between two node : Euclidian distance
    def distance(self, node):
        dist_x = pow((self.x - node.x), 2)
        dist_y = pow((self.y - node.y), 2)
        result = round(pow(dist_x + dist_y, (1/2)))
        return result


fh = open('Texts\example-input-1.txt', 'r')
rec = fh.readline().rstrip("\n")
temp = 0
nodes = []
while rec != "":
    temp1 = 0
    temp2 = 0
    temp = Node(0, 0, 0)
    for i in range(0, len(rec)):
        if rec[i] == " " or i == len(rec) - 1:
            if temp2 == 0:
                temp.id = int(rec[temp1:i + 1])
                temp1 = i + 1
                temp2 = 1
            elif temp2 == 1:
                temp.x = int(rec[temp1:i + 1])
                temp1 = i + 1
                temp2 = 2
            else:
                temp.y = int(rec[temp1:i + 1])
                temp1 = i + 1
    rec = fh.readline().rstrip("\n")
    nodes.append(temp)

sol, tot = greedy_algorithm(nodes)

file = open('Texts\solution1.txt', 'w')
file.write(str(tot) + "\n")

for i in range(0, len(sol)):
    file.write(str(sol[i].id) + "\n")