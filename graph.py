# graph representation - directed, undirected graph
# graph consist of node and edges
# graph can be created by => ADJACENCY_MATRIX, ADJACENCY_LIST
# in the below structure nodes are names and edges are |,-
# facebook     Undirected graph
#                 ashok_patel ---- minish_kumar
#                      |
#                      |
# rohit_sharma ---- rohan_kumar ---- mohammed_shami
#                       |
#                       |
#                   yami_gautam             
# 
# 
alp = [chr(i) for i in range(97,123)]
def create_matrix(rows, columns, data):
    mat = []
    for i in range(rows):
        ls = []
        for j in range(columns):
            ls.append(data[i*rows+j])
        mat.append(ls)
    return mat
mat = create_matrix(5, 5, alp)
# print(mat)

# ========================================================================================================================
#     ∞ => no value ie infinity                                 UNDIRECTED_GRAPH
# ADJACENCY MATRIX                                            0    1    2     3                0     1    2     3      
#          ___       40    ___                               ____________________            ______________________
#         | 0 |-----------| 1 |                          0  | N  | Y  | Y  |  Y  |         0 | ∞  | 40 | 20 |  10 |
#          ---  \          ---                              |____|____|____|_____|           |____|____|____|_____|
#           |    \           |                           1  | Y  | N  | Y  |  N  |         1 | 40 | ∞  | 15 |  ∞  |
#           |     \          |                              |____|____|____|_____|           |____|____|____|_____|
#       10  |      \ 20      | 15                        2  | Y  | Y  | N  |  Y  |         2 | 20 | 15 | ∞  |  4  |
#           |       \        |                              |____|____|____|_____|           |____|____|____|_____|
#           |        \       |                           3  | Y  | N  | Y  |  N  |         3 | 10 | ∞  | 4  |  ∞  |
#         ___               ___                             |____|____|____|_____|           |____|____|____|_____|
#        | 3 |-------------| 2 |
#         ---       4       ---

# ========================================================================================================================
#  UNDIRECTED_GRAPH     => in ADJACENCY_LIST  it can represented by either LIST or TUPLE

#                                   0    1    2    3
# ADJACENCY_LIST                   ____________________
#      ___        ___          0  | N  | N  | Y  |  N  |    
#     | 0 |      | 1 |            |____|____|____|_____|    
#      --- \     /---          1  | N  | N  | N  |  Y  |  
#           \   /                 |____|____|____|_____|
#            \ /               2  | Y  | N  | N  |  Y  |
#            / \                  |____|____|____|_____|
#           /   \              3  | N  | Y  | Y  |  N  |
#     ___  /     \  ___           |____|____|____|_____|
#    | 3 | --------| 2 |
#     ---           ---  
# 

#  graph = {0:[2], 1:[3], 2:[0, 3], 3:[1, 2]}
#                   | 
#                   v
# 
#                   10
#               0 ------- 2
#                        /   
#                       /15
#                      / 
#                     3 -------- 1
#                           25
# 
# weighted undirected graph for adjacency list
# graph = {0:[(2, 10)], 2:[(0, 10), (3, 15)], 3:[(2, 15), (1, 25)], 1:[(3, 25)]}      

# input can be taken in the form of U,V,W => where U is startNode, V is endNode and W is cost of going from start to endNode
# 1. ADJACENCY_MATRIX, NODE_COUNT = 5
# adj_Matrix = [[float('-inf') for i in range(5)] for j in range(5)]
# print(adj_Matrix)
# DIRECTED_GRAPH
# for i in range(10):
#     u, v, w = map(int, input("Enter a three value: ").split())
#     adj_Matrix[u][v] = w
# print(adj_Matrix)

# UNDIRECTED_GRAPH
# for i in range(5):
#     u, v, w = map(int, input("enter the nodes with weight ").split())
#     adj_Matrix[u][v] = w
#     adj_Matrix[v][u] = w
# print(adj_Matrix)

# 2. ADJACENCY_LIST, NODE_COUNT = 5
adj_list = {}
# DIRECTED_GRAPH
# for i in range(5):
#     u, v, w = map(int, input('Enter the key value ').split())
#     if u in adj_list:
#         adj_list[u].append([(v, w)])
#     else:
# #    #    adj_list[u] = [(v, w)]    #below code is same as this but this is single line code
#         adj_list[u] = []
#         adj_list[u].append((v, w))
# print(adj_list)

# UNDIRECTED_GRAPH
for i in range(5):
    u, v, w = map(int, input("Enter the nodes and weight ").split())
    if u in adj_list:
        adj_list[u].append((v, w))
    else:
        adj_list[u] = []
        adj_list[u].append((v, w))
    if v in adj_list:
        adj_list[v].append((u, w))
    else:
        adj_list[v] = []
        adj_list[v].append((u, w))

print(adj_list)
# ======================================================================================================================== 
     
                    
# flight routes     Directed graph

#       >  paris   \
#      /      |     \
#     /       |      >
# mumbai      |    newyork  \ 
#     \       |       >      \
#      \      |      /        \
#       \     v     /          \>
#        \>  delhi /         toronto

# routes b/w two cities   mumbai & newyork
# A. all possible routes for above cities 
# 1. mumbai -> paris -> newyork
# 2. mumbai -> delhi -> newyork
# 3. mumbai -> paris -> delhi -> newyork
# B. get shortest distances (min-stops)
# 1. mumbai -> paris -> newyork
# 2. mumbai -> delhi -> newyork
from PIL import Image
img = Image.open('/mnt/A4B278D5B278AD84/Python+ml Crash Course/pythonPracticeQuest/logic/graph.png')
# img.show()

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dic = {}
        for k, v in self.edges:
            if k in self.graph_dic:
                self.graph_dic[k].append(v)
            else:
                self.graph_dic[k] = [v]
        # print(self.graph_dic)

    #start -> source, end -> destination
    def get_path(self, start, end, path = []):
        #start = mumbai, end = newyork
        # 1. mumbai --> paris --> newyork
        # 2. mumbai --> dubai --> newyork
        # 3. mumbai --> paris --> dubai --> newyork
        path = path + [start]
                                            # s='Paris',e='New York',p=['Mumbai'] 
        #start and end are same                 p = ['Mumbai', 'Paris']
        if start == end:
            return [path]                   #s='Dubai',e='New York',p=['Mumbai', 'Paris']
                                                #p = ['Mumbai', 'Paris', 'Dubai']
        #corner case
        if start not in self.graph_dic:
            return []

        paths = []
        # mumbai -> paris -> dubai -> newyork
        for node in self.graph_dic[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dic:
            return
        shortest_path = None
        for node in self.graph_dic[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                # print(sp)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path
        

if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')
    ]
    # d = {
    #     'Mumbai': ['Paris', 'Dubai'],
    #     'Paris': ['Dubai', 'New York'],
    #     'Dubai': ['New York'],
    #     'New York': ['Toronto']
    # }
    routes_graph = Graph(routes)
    start = 'Mumbai'
    end = 'New York'
    # print(f'Route between {start} and {end}',routes_graph.get_path(start, end))
    # print(f'Shortest path between {start} and {end}',routes_graph.get_shortest_path(start, end))