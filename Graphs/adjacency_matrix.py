class Graph:
    def __init__(self,vertices):
        self.mat=[[0]*vertices for _ in range(vertices)]
        self.size=vertices


  # For UNDIRECTED GRAPH

    def add_edge_UNDIRE(self,src,dest):
        if(0<=src<self.size and 0<=dest<self.size):
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            print("Invalid Edge") 

    

    # For DIRECTED GRAPH

    def add_edge_DIRECT(self,src,dest):
        if(0<=src<self.size and 0<=dest<self.size):
            self.mat[src][dest]=1
        else:
            print("Invalid Edge") 

    # For Weighted GRAPH
    def add_edge_WEIGHTED(self,src,dest,weight):
        if(0<=src<self.size and 0<=dest<self.size):
            self.mat[src][dest]=weight
        else:
            print("Invalid Edge") 

    def Print(self):
        for row in self.mat:
            print(" ".join(map(str,row)))

g=Graph(5)
g.add_edge_UNDIRE(0,1)
g.add_edge_UNDIRE(0,2)
g.add_edge_UNDIRE(1,3)
g.add_edge_UNDIRE(2,3)
g.add_edge_UNDIRE(3,4)
g.Print()