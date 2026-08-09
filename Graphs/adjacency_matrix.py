class Graph:
    def __init__(self, vertices):
        self.matrix = [[0] * vertices for _ in range(vertices)]
        self.size = vertices

    def add_edge(self, src, dest):
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.matrix[src][dest] = 1
            self.matrix[dest][src] = 1   # undirected graph
        else:
            print("Invalid edge")

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))


a = Graph(5)
a.add_edge(0, 1)
a.add_edge(0, 4)
a.add_edge(1, 2)
a.add_edge(1, 3)
a.add_edge(1, 4)
a.add_edge(2, 3)
a.add_edge(3, 4)

print("Adjacency Matrix:")
a.print_matrix()