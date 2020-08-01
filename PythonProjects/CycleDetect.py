import collections

noCycle = {
    "A": set(["B"]),
    "B": set(["E", "C"]),
    "C": set(["D"]),
    "D": set([]),
    "E": set(["C"])
}

cycle = {
    "A": set(["B"]),
    "B": set(["E", "C"]),
    "C": set(["D", "B"]),
    "D": set([]),
    "E": set(["C"])
}

def stackDfs(graph):
    stack = collections.deque()
    visited = set()
    if len(graph) == 0:
        return
    stack.append(list(graph.keys())[0])

    while(len(stack) > 0):
        curr = stack.pop()
        print(f'{curr}, {visited}')
        for node in graph[curr]:
            if node not in visited:
                stack.append(node)
                # WHEN USING A STACK DS, YOU MUST WRITE TO VISITED EVERY TIME YOU APPEND TO STACK
                # or else you may end up visiting the same node twice if there are two paths to it (both neighbours append node 'E' to the stack without marking it as visited)
                visited.add(node)

def dfsHelper(current, visited, active, graph):
    visited.add(current)
    active.add(current)
    # WHEN USING A RECURSIVE STACK, IT IS ENOUGH TO WRITE TO VISITED AT THE BEGINNING OF EACH CALL
    # print(f'{current}, {visited}')
    print(f'{current}, {visited}, {active}')
    for node in graph[current]:
        if node in active:
            print(f'Error, {node} currently active')
            return True
        elif node not in visited:
            if dfsHelper(node, visited, active, graph):
                return True
    active.remove(current)
    return False
    


def detectCycle(graph):
    visited = set()
    active = set()
    first = list(graph.keys())[0]
    if len(graph) == 0:
        return False
    else:
        return dfsHelper(first, visited, active, graph)

if __name__ == "__main__":
    print(detectCycle(cycle))
    print("")
    print(detectCycle(noCycle))