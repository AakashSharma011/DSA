class Graph:
    def __init__(self):
        self.adjlist={}

    def add_vertex(self,vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex]=[]

    def add_edge(self,src,dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adjlist[src].append(dest) 
        self.adjlist[dest].append(src)  # undirected graph

    def print_graph(self):
        for vertex in self.adjlist:
            print(vertex,"->",end=" ")
            print(" ".join(map(str,self.adjlist[vertex])))

g=Graph()
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_graph()