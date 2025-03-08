class GraphAdjMatrix:
    def __init__(self, num_nodes):
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.num_nodes = num_nodes

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # Für ungerichtete Graphen

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def has_path(self, u, v):
        return self.matrix[u][v] == 1
