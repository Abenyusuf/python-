from Graph import Vertex, Graph
from Queue import Queue


def breadth_first_search(graph, start_vertex, distances=dict()):
    if distances is None:
        distances = dict()
    frontier_queue = Queue()  # queue to store vertices
    discovered_set = set()  # set to store discovered vertices
    visited_list = []  # list to store visited vertices

    distances[start_vertex] = 0  # distance from start_vertex to itself is 0

    frontier_queue.enqueue(start_vertex)  # enqueue or add start_vertex in the frontier queue
    discovered_set.add(start_vertex)  # add start_vertex to the discovered set

    # while there are vertices to visit in the frontier queue
    while frontier_queue.list.head is not None:
        current_vertex = frontier_queue.dequeue()  # dequeue the vertex at the head of the frontier queue
        visited_list.append(current_vertex)  # add the dequeued vertex to the visited_list

        # explore adjacent vertices of the current_vertex
        for adj_vertex in graph.adjacency_list[current_vertex]:
            if adj_vertex not in discovered_set:  # if adjacent vertex not discovered yet
                frontier_queue.enqueue(adj_vertex)  # enqueue the adjacent vertex
                discovered_set.add(adj_vertex)  # mark it as discovered

                # distance of the adjacent vertex must be more than current vertex
                # we add 1 to the adjacent vertex's distance
                distances[adj_vertex] = distances[current_vertex] + 1

    return visited_list  # return the visited vertices in traversal order


# main program
social_graph = Graph()  # create an instance of the graph class

# create vertex instances representing individuals in the graph
joe = Vertex('Joe')
eva = Vertex('eva')
taj = Vertex('Taj')
chen = Vertex('Chen')
lily = Vertex('Lily')
jun = Vertex('Jun')
ken = Vertex('Ken')


# store vertices in a list for easy access
vertices = [joe, eva, taj, chen, lily, jun, ken]

for v in vertices:
    social_graph.add_vertex(v)

# add edges between vertices to represent connections
social_graph.add_undirected_edge(joe, eva)  # edge from joe to eva
social_graph.add_undirected_edge(joe, taj)  # edge from joe to taj
social_graph.add_undirected_edge(eva, lily)
social_graph.add_undirected_edge(taj, chen)
social_graph.add_undirected_edge(taj, lily)
social_graph.add_undirected_edge(chen, jun)
social_graph.add_undirected_edge(lily, jun)
social_graph.add_undirected_edge(jun, ken)

# ask user to input the starting name
start_name = input('enter the starting name:')
print()

# search for the start vertex withing the list of vertices
start_vertex = None
for v in vertices:
    if v.label == start_name:  # if users vertex label matches the users input
        start_vertex = v

vertex_distances = dict()
visited_list = breadth_first_search(social_graph, start_vertex, vertex_distances)
# display the graph

for v in visited_list:
    print('%s: %d' % (v.label, vertex_distances[v]))

social_graph.display_graph()
