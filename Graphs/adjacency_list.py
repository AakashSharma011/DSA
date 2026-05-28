class Graph:
    def __init__(self):
        self.adjlist={}
    
    def add_vertex(self,vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex]=[]
    
    def add_edge(self,src,dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adjlist[src].append(dest)  # end here for directed graph
        self.adjlist[dest].append(src)  # end here for undirected graph

    def printGraph(self):
        for vertex in self.adjlist:
            print(vertex,"-->",self.adjlist[vertex],end="\n")


g=Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(3,4)
g.add_edge(2,3)
g.add_edge(4,5)
g.add_edge(5,3                            )
g.printGraph()