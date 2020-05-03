class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.nodes:
            self.add_node(v1)
        if v2 not in self.nodes:
            self.add_node(v2)
        self.nodes[v2].add(v1)

    def get_neighbors(self, node):
        return self.nodes[node]