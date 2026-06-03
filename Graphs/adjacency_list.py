class Graph:
    def __init__(self) -> None:
        self.adj_list: dict[int, list[int]] = {}
    
    def add_vertex(self, vertex: int) -> None:
        """
        Adds a vertex to the graph if it doesn't already exist.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, src: int, dest: int) -> None:
        """
        Adds an undirected edge between src and dest.
        Automatically adds the vertices if they do not exist.
        """
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def print_graph(self) -> None:
        """
        Prints the adjacency list representation of the graph.
        """
        for vertex in sorted(self.adj_list.keys()):
            print(f"{vertex} --> {self.adj_list[vertex]}")


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 3)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    
    print("Graph Adjacency List:")
    g.print_graph()