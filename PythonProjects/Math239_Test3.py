# Adjacency Matrix representation in Python
from itertools import combinations

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end='')
            print()


def countSpanningTrees(current: int, visited: set, n: int, g:Graph) -> int:   
    currentEdges = [i for i, j in  enumerate(g.adjMatrix[current]) if j == 1]
    count = 0
    # For a combination of i edges
    for i in range(1, len(currentEdges) + 1):
        edgeCombinations = combinations(currentEdges, i)

        for combination in edgeCombinations:
            # Each combination of edges on the current node
            print(current, combination)
            valid = True
            for edge in combination:
                if edge in visited:
                    # This combination of edges does not create a spanning tree
                    valid = False
            if valid:
                for edge in combination:
                    visited.add(edge)

                if len(visited) == n:
                    count += 1
                    print("yes")
                else:
                    for edge in combination:
                        count += countSpanningTrees(edge, visited, n, g)

                for edge in combination:
                    visited.remove(edge)
    
    return count

def main():
    n = input("Give n: ")
    n = int(n)
    g = Graph(3 + n)

    # Edges between the abc
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    
    # Edges between abc and the other part
    for i in range(n): # For each vertex in the other part
        g.add_edge(3 + i, 0) 
        g.add_edge(3 + i, 1) 
        g.add_edge(3 + i, 2) 

    g.print_matrix()


    # Find spanning trees
    visited = set()
    visited.add(0)
    count = countSpanningTrees(0, visited, 3+n, g)
    print("The count is " + str(count))


if __name__ == '__main__':
    main()
