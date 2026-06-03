class Graph:
    def __init__(self, vertices: int) -> None:
        self.size = vertices
        self.mat = [[0] * vertices for _ in range(vertices)]

    def add_edge_undirected(self, src: int, dest: int) -> None:
        """
        Adds an undirected edge between src and dest.
        """
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge")

    def add_edge_directed(self, src: int, dest: int) -> None:
        """
        Adds a directed edge from src to dest.
        """
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1
        else:
            print("Invalid Edge")

    def add_edge_weighted(self, src: int, dest: int, weight: int) -> None:
        """
        Adds a weighted edge from src to dest with the given weight.
        """
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = weight
        else:
            print("Invalid Edge")

    def print_matrix(self) -> None:
        """
        Prints the adjacency matrix.
        """
        for row in self.mat:
            print(" ".join(map(str, row)))


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge_undirected(0, 1)
    g.add_edge_undirected(0, 2)
    g.add_edge_undirected(1, 3)
    g.add_edge_undirected(2, 3)
    g.add_edge_undirected(3, 4)
    
    print("Graph Adjacency Matrix:")
    g.print_matrix()