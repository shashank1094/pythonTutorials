from collections import defaultdict
from typing import List

# https://stackoverflow.com/questions/46506077/how-to-detect-cycles-in-a-directed-graph-using-the-iterative-version-of-dfs/62971341#62971341
class SolutionIterative:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class Color:
            WHITE = "white"
            GRAY = "gray"
            BLACK = "black"
        adjacent_list = defaultdict(list)
        for _destination, _source in prerequisites:
            adjacent_list[_source].append(_destination)
        color_per_course = [Color.WHITE] * numCourses
        courses_order = []
        try:
            for course in range(numCourses):
                if color_per_course[course] == Color.WHITE:
                    stack = [course]
                    while stack:
                        current_course = stack[-1]
                        if color_per_course[current_course] == Color.WHITE:
                            # print(current_course, stack, color_per_course, courses_order)
                            color_per_course[current_course] = Color.GRAY
                            for neighbour_course in adjacent_list[current_course]:
                                if color_per_course[neighbour_course] == Color.WHITE:
                                    stack.append(neighbour_course)
                                if color_per_course[neighbour_course] == Color.GRAY:
                                    raise Exception("Found cycle in the graph")
                        elif color_per_course[current_course] == Color.GRAY:
                            color_per_course[current_course] = Color.BLACK
                            courses_order.append(current_course)
                            stack.pop()
                        elif color_per_course[current_course] == Color.BLACK:
                            stack.pop()
        except Exception:
            return []
        return courses_order[::-1]

class SolutionRecursive:
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)
        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        topological_sorted_order = []
        is_possible = True
        # By default, all vertices are WHITE
        color = {k: self.WHITE for k in range(numCourses)}

        def dfs(node: int) -> None:
            nonlocal is_possible
            # Don't recurse further if we found a cycle already
            if not is_possible:
                return
            # Start the recursion
            color[node] = self.GRAY
            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == self.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == self.GRAY:
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False
            # Recursion ends. We mark it as black
            color[node] = SolutionRecursive.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == self.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []

if __name__ == '__main__':
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    num_of_courses = 4
    print(SolutionRecursive().findOrder(num_of_courses, prerequisites))
    print(SolutionIterative().findOrder(num_of_courses, prerequisites))
    prerequisites.append([0, 3])
    print(SolutionRecursive().findOrder(num_of_courses, prerequisites))
    print(SolutionIterative().findOrder(num_of_courses, prerequisites))