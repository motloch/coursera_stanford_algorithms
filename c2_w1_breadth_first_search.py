"""
Algorithm for finding shortest distances to all vertices of a graph using Breadth First
Search 

Based on the Week One of the 'Graph Search, Shortest Paths, and Data Structures' course on
Coursera (Algorithms Specialization, Stanford University) 
"""

class Graph:
    """
    Representation of an oriented graph
    """

    def __init__(self, N, edges_from_vertices):
        """
        Initialize a graph 
        
        param N: number of vertices of the graph
        param edges_from_vertices: list of lists, it's n-th element is a list of edges from
                                        vertex number n (zero based indexing)
        """
        self.N = N
        self.edges_from_vertices = edges_from_vertices
    

def find_shortest_path(g, starting_vertex):
    """
    Starting from a vertex, return an array with minimal number of steps necessary to each
    vertex in a graph (or -1 if vertex not reachable)

    param g: instance of class Graph, representing the oriented graph
    param starting_vertex: number of the vertex we start from (zero based indexing)

    return: array of length g.N (-1 or non-negative integers)
    """

    #Initialize all vertices as unreachable
    out = [-1 for x in range(g.N)]

    #Initialize the breadth first search
    out[starting_vertex] = 0
    queue = [starting_vertex]

    #Iterate while we have unprocessed vertices
    while len(queue) > 0:

        current_vertex = queue.pop(0)
        neighbors = g.edges_from_vertices[current_vertex]

        #Check vertices reachable from current vertex
        for n in neighbors:
            if out[n] == -1:        #Is it newly discovered?
                out[n] = out[current_vertex] + 1
                queue.append(n)

    return out

if __name__ == "__main__":
    #Test it out on a simple example
    g = Graph(6, [[1, 2], [3], [3, 4], [5], [5], []])
    assert(find_shortest_path(g, 0) == [0, 1, 1, 2, 2, 3])
