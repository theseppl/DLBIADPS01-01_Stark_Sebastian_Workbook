class GraphAdjMatrix:
    def __init__(self, num_nodes, gerichtet=False):
        if num_nodes > 26:
            raise ValueError("Die maximale Anzahl der Knoten beträgt 26 (A bis Z).")
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.num_nodes = num_nodes
        self.node_labels = [chr(i) for i in range(65, 65 + num_nodes)]  # 'A' bis 'Z'
        self.gerichtet = gerichtet  # Eigenschaft für gerichteten oder ungerichteten Graphen

    def hinzufügenKante(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        self.matrix[u_index][v_index] = 1
        if not self.gerichtet:
            self.matrix[v_index][u_index] = 1  # Nur bei ungerichteten Graphen

    def entfernenKante(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        self.matrix[u_index][v_index] = 0
        if not self.gerichtet:
            self.matrix[v_index][u_index] = 0  # Nur bei ungerichteten Graphen

    def istKanteVorhanden(self, u, v):
        u_index = self.node_labels.index(u)
        v_index = self.node_labels.index(v)
        return self.matrix[u_index][v_index] == 1

    def zeigeMatrix(self):
        print("Adjazenzmatrix:")
        print("  " + " ".join(self.node_labels))  # Spaltenüberschriften
        for i, row in enumerate(self.matrix):
            print(self.node_labels[i] + " " + " ".join(map(str, row)))

matrix = GraphAdjMatrix(4, False)
matrix.hinzufügenKante('A','B')
matrix.hinzufügenKante('A','A')
matrix.zeigeMatrix()
