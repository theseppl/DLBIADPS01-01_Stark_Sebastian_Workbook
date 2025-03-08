class GraphAdjMatrix:
    def __init__(self, num_nodes, directed=False):
        if num_nodes > 26:
            raise ValueError("Die maximale Anzahl der Knoten beträgt 26 (A bis Z).")
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.num_nodes = num_nodes
        self.node_labels = [chr(i) for i in range(65, 65 + num_nodes)]  # 'A' bis 'Z'
        self.directed = directed  # Eigenschaft für gerichteten oder ungerichteten Graphen

    def add_edge(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        self.matrix[u_index][v_index] = 1
        if not self.directed:
            self.matrix[v_index][u_index] = 1  # Nur bei ungerichteten Graphen

    def remove_edge(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        self.matrix[u_index][v_index] = 0
        if not self.directed:
            self.matrix[v_index][u_index] = 0  # Nur bei ungerichteten Graphen

    def has_path(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        return self.matrix[u_index][v_index] == 1

    def display_matrix(self):
        print("Adjazenzmatrix:")
        print("  " + " ".join(self.node_labels))  # Spaltenüberschriften
        for i, row in enumerate(self.matrix):
            print(self.node_labels[i] + " " + " ".join(map(str, row)))

matrix = GraphAdjMatrix(4, True)
matrix.add_edge('A','B')
matrix.add_edge('A','A')
matrix.display_matrix()
