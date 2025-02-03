import networkx as nx
import matplotlib.pyplot as plt


class Graph:
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