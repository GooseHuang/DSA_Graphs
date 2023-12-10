#
#
# # Node
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.neighbor = None
#
#
# # Adjacency List
# class Edge:
#     def __init__(self, node1, node2, weight):
#         self.a = node1
#         self.b = node2
#         self.weight = weight
#

# Graph in Adjacent Matrix
# class Graph:
#     def __init__(self):
#         self.matrix = {}
#
#     def add_node(self, node):
#         self.matrix[node] = dict()
#
#     def add_edge(self, node1, node2, value):
#         self.matrix[node1][node2] = value
#         self.matrix[node2][node1] = value
#
#     def remove_edge(self, node1, node2):
#         self.matrix[node1].remove(node2)
#         self.matrix[node2].remove(node1)
#
#     def remove_node(self, node):
#         self.matrix.pop(node)


class Graph:
    def __init__(self):
        self.matrix = {}

    def add_node(self, node):
        self.matrix[node] = set()

    def add_edge(self, node1, node2):
        self.matrix[node1].add(node2)
        self.matrix[node2].add(node1)

    def remove_edge(self, node1, node2):
        self.matrix[node1].remove(node2)
        self.matrix[node2].remove(node1)

    def remove_node(self, node):
        self.matrix.pop(node)


def search(graph, start_node):
    matrix = graph.matrix

    stack = list(matrix[start_node])
    connected_set = set()
    connected_set.add(start_node)
    while stack:
        first = stack.pop(0)
        connected_set.add(first)
        for x in matrix[first]:
            if not x in connected_set:
                stack.append(x)

    # for x in connected_set:
    #     if x!=start_node:
    #         print(x)
    return connected_set

def get_connect_info(graph, node1, node2):
    connected_set = search(graph, node1)
    if node2 in connected_set:
        return True
    else:
        return False



# Find Path
def find_path():
    pass

def main():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('C', 'D')

    connected_set = search(g, 'A')
    start_node = 'A'
    for x in connected_set:
        if x != start_node:
            print(x)

    connect_info = get_connect_info(g, 'A', 'D')
    print("A->D:", connect_info)

    connect_info = get_connect_info(g, 'A', 'E')
    print("A->E:", connect_info)


if __name__=='__main__':
    main()

