from Graph import Vertex, Graph


# depth_first search function
def depth_first_search(graph, start_vertex, visit_function):
    # initialize a stack with the start vertex
    vertex_stack = [start_vertex]
    # initialize an empty set to keep track of the visited vertices
    visited_set = set()

    # while there are vertices in the stack
    while len(vertex_stack) > 0:
        # pop the top vertex from the stack
        current_v = vertex_stack.pop()

        # check if the current vertex hasn't been visited
        if current_v not in visited_set:
            # visit the current vertex
            # by calling the visit function on the current vertex
            visit_function(current_v)

            # add the current vertex to the visited set
            visited_set.add(current_v)

            # for each adjacent vertex to the current vertex
            for adj_v in graph.adjacency_list[current_v]:
                # push the adjacent vertex to the stack
                vertex_stack.append(adj_v)


# definition for the visit function
def visit(vertex):
    print(vertex.label, end=',')


# main program
# create a list of vertex labels
vertex_names = ['A', 'B', 'C', 'D', 'E', 'F']

# create an empty graph instance
graph1 = Graph()

for v in vertex_names:
    graph1.add_vertex(Vertex(v))

# create edges
graph1.add_undirected_edge(graph1.get_vertex('A'), graph1.get_vertex('B'))
graph1.add_undirected_edge(graph1.get_vertex('A'), graph1.get_vertex('D'))

# show the graph
graph1.display_graph()
