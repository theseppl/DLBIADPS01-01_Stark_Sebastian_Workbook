class GraphAdjMatrix:
    def __init__(self, num_nodes):
        if num_nodes > 26:
            raise ValueError("Die maximale Anzahl der Knoten beträgt 26 (A bis Z).")
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.num_nodes = num_nodes
        self.node_labels = [chr(i) for i in range(65, 65 + num_nodes)]  # 'A' bis 'Z'

    def add_edge(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        self.matrix[u_index][v_index] = 1
        self.matrix[v_index][u_index] = 1  # Für ungerichtete Graphen

    def remove_edge(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        self.matrix[u_index][v_index] = 0
        self.matrix[v_index][u_index] = 0

    def has_path(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        return self.matrix[u_index][v_index] == 1

    def display_matrix(self):
        print("Adjazenzmatrix:")
        print("  " + " ".join(self.node_labels))  # Spaltenüberschriften
        for i, row in enumerate(self.matrix):
            print(self.node_labels[i] + " " + " ".join(map(str, row)))  # Zeilenüberschriften


matrix = GraphAdjMatrix(4)
matrix.add_edge('A','B')
matrix.add_edge('A','A')
matrix.display_matrix()
