class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, Vnum):
        self.Vnum = Vnum
        self.graph = [None] * self.Vnum

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

  

# if __name__ == "__main__":
#     V = 5

#     # Create graph and edges
#     graph = Graph(V)
#     graph.add_edge(0, 1)
#     graph.add_edge(0, 2)
#     graph.add_edge(0, 3)
#     graph.add_edge(1, 2)
#     print(graph.graph[0])

#     graph.print_agraph()