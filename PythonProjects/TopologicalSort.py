import collections

noCycle = {
    "A": set(["B"]),
    "B": set(["E", "C"]),
    "C": set(["D"]),
    "D": set([]),
    "E": set(["F","C"]),
    "F": set(["G"]),
    "G": set(["C"]),
    "Z": set(["B"])
}

def DFSUtil(current, visited, graph, order):
    visited.add(current)
    
    for node in graph[current]:
        if node not in visited:
            DFSUtil(node, visited, graph, order)
    order.appendleft(current)

def TopologicalSort(graph):
    order = collections.deque()
    visited = set()

    for node in graph.keys():
        if node not in visited:
            DFSUtil(node, visited, graph, order)
    return order

if __name__ == '__main__':
    print(TopologicalSort(noCycle))