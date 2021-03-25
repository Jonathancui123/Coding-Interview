# Dependency graph --> courses depend on one another
# Idea: Cycle detection algorithm

# Each course is a node, nodes point at the courses they depend on

# 1. Build a graph out of the courses

# 2. Loop through 'visited' array. Upon a node that hasn't been visited, perform the following:

# {
# 3. Recursive call stack nodes that we are about to visit , (like depth first search)
# Keep a 'visiting' array, and a 'visited array' --> the index of the array refers to the course
# 4. For each node, mark it as "visiting" and call the function on its children. 
#     Base case: No children/already visited - return true, remove from 'visiting' move to 'visited'
#     Base case 2: it is in 'visiting' --> indicates cycle found - return false
# 5. If all function calls on children return true -> return true, else return false. Remove from 'visiting' and move to visited.
# } --> if the result is false, we have a loop. Return false

# All nodes visited --> no cycle.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for course, req in prerequisites:
            graph[course].append(req)
        
        visiting = [False] * numCourses
        visited = [False] * numCourses
        
        i = 0
        while i < numCourses:
            if (not self.checkDeps(i, visited, visiting, graph)):
                return False
            i += 1

        return True
        
    def checkDeps(self,currCourse, visited, visiting, graph):
        if (visiting[currCourse]):
            return False
        if (visited[currCourse] or len(graph[currCourse]) == 0):
            return True
        visiting[currCourse] = True
        for childCourse in graph[currCourse]:
            if (not self.checkDeps(childCourse, visited, visiting, graph)):
                return False
        visiting[currCourse] = False
        visited[currCourse] = True

        return True
            
                    
        