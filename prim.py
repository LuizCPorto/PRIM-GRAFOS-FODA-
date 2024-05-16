import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

def prim(graph):
    visited = set()
    edges = []
    total_weight = 0

    # Starting from the first vertex
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    while len(visited) != len(graph):
        min_weight = float('inf')
        min_edge = None

        # Iterate over visited vertices
        for u in visited:
            # Check neighboring vertices
            for v, weight in graph[u]:
                if v not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (u, v)

        if min_edge:
            u, v = min_edge
            visited.add(v)
            edges.append((u, v, min_weight))
            total_weight += min_weight

    return edges, total_weight

# Create a graph instance
g = Graph()

# Add edges with weights
g.addEdge('v6', 'v1', 1)
g.addEdge('v6', 'v2', 2)
g.addEdge('v6', 'v3', 2)
g.addEdge('v6', 'v5', 4)
g.addEdge('v6', 'v4', 6)
g.addEdge('v1', 'v2', 6)
g.addEdge('v1', 'v3', 5)
g.addEdge('v3', 'v5', 4)
g.addEdge('v2', 'v4', 5)
g.addEdge('v4', 'v5', 3)

# Calculate minimum spanning tree using Prim's algorithm
min_spanning_tree, total_weight = prim(g.graph)

# Create a networkx graph from the minimum spanning tree edges
G = nx.Graph()
for u, v, weight in min_spanning_tree:
    G.add_edge(u, v, weight=weight)

# Plot the minimum spanning tree
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
plt.axis("off")
plt.title("Minimum Spanning Tree")
plt.show()
