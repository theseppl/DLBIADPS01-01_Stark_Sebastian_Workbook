class GraphAdjMatrix:
    def __init__(self, num_nodes, gerichtet=False):
        if num_nodes > 26:
            raise ValueError("Die maximale Anzahl der Knoten beträgt 26 (A bis Z).")
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.num_nodes = num_nodes
        self.node_labels = [chr(i) for i in range(65, 65 + num_nodes)]  # 'A' = ASCII 65 / 'B' = ASCII 66...
        self.gerichtet = gerichtet  # Eigenschaft für gerichteten oder ungerichteten Graphen

    def hinzufuegenKante(self, u, v):
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
        if self.matrix[u_index][v_index] == 1:
            print(f"Es existiert eine Kante zwischen {u} und {v}.")
        else:
            print(f"Es existiert keine Kante zwischen {u} und {v}.")

    def zeigeMatrix(self):
        graph_type = "Gerichteter Graph" if self.gerichtet else "Ungerichteter Graph"
        print(f"{graph_type} - Adjazenzmatrix:")
        print("  " + " ".join(self.node_labels))  # Spaltenüberschriften
        for i, row in enumerate(self.matrix):
            print(self.node_labels[i] + " " + " ".join(map(str, row)))

matrix = GraphAdjMatrix(4, False)
matrix.hinzufuegenKante('A','A')
matrix.hinzufuegenKante('A','C')
matrix.hinzufuegenKante('C','D')
matrix.hinzufuegenKante('D','B')

matrix.hinzufuegenKante('C', 'B')
matrix.istKanteVorhanden('B', 'C')
matrix.entfernenKante('C', 'B')
matrix.istKanteVorhanden('B', 'C')
matrix.zeigeMatrix()
