
import networkx as nx # "pip install networkx", for graph implementation
import matplotlib.pyplot as plt # "pip install matplotlib", for plotting

class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
        
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

# return the vertex in the graph with the specified label
# if no such vertex exists, return None
    def get_vertex(self, vertex_label):
        for v in self.adjacency_list:  # loop all adjacent vertices
            if v.label == vertex_label:  # compare vertex labels
                return v  # vertex found
            return None  # vertex not found

    def display_graph(self):
        G = nx.DiGraph()  # Create a directed graph

        # Add nodes
        for vertex in self.adjacency_list:
            G.add_node(vertex.label)

        # Add edges
        for from_vertex in self.adjacency_list:
            for to_vertex in self.adjacency_list[from_vertex]:
                G.add_edge(from_vertex.label, to_vertex.label, weight=self.edge_weights[(from_vertex, to_vertex)])

        # Position nodes using spring layout
        pos = nx.spring_layout(G)
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # Draw edges
        nx.draw_networkx_edges(G, pos, width=2)

        # Draw edge labels
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Draw node labels
        node_labels = {node: node for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=node_labels)

        # Show plot
        plt.title("Graph Visualization")
        plt.axis("off")
        plt.show()
