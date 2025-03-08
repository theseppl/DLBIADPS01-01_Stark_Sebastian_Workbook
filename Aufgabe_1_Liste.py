class GraphAdjList:
    def __init__(self, num_nodes, gerichtet=False):
        if num_nodes > 26:
            raise ValueError("Die maximale Anzahl der Knoten beträgt 26 (A bis Z).")
        self.adj_list = {chr(i): [] for i in range(65, 65 + num_nodes)}  # 'A' bis 'Z'
        self.num_nodes = num_nodes
        self.gerichtet = gerichtet  # Eigenschaft für gerichteten oder ungerichteten Graphen

    def hinzufügenKante(self, u, v):
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if not self.gerichtet and u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def entfernenKante(self, u, v):
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if not self.gerichtet and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def istKanteVorhanden(self, u, v):
        graph_type = "Gerichteter Graph" if self.gerichtet else "Ungerichteter Graph"
        print(f"{graph_type}:")
        if v in self.adj_list[u]:
            print(f"Es existiert eine Kante zwischen {u} und {v}.")
        else:
            print(f"Es existiert keine Kante zwischen {u} und {v}.")

    def zeigeListe(self):
        graph_type = "Gerichteter Graph" if self.gerichtet else "Ungerichteter Graph"
        print(f"{graph_type} - Adjazenzliste:")
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {', '.join(neighbors) if neighbors else 'Keine Nachbarn'}")
