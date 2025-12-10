class GraphMatrix:
    def __init__(self, n):
        self.n = n
        self.mat = [[0]*n for _ in range(n)]

    def add_edge(self, u, v):
        self.mat[u][v] = 1

    def display(self):
        for row in self.mat:
            print(row)

g = GraphMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.display()