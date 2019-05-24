

class Solution:
    def isBipartite(self, graph):
        self.colors = {}
        self.GRAY = 1
        self.BLACK = 2
        self.WHITE = 3
        for i in range(len(graph)):
            self.colors[i] = self.GRAY
        return self.util(graph)

    def util(self, g):
        queue = [0]
        visited = {}

        while len(queue) != 0 and len(visited) != len(g):
            first_elem_indx = queue.pop(0)
            visited[first_elem_indx] = True
            curr_color = self.colors[first_elem_indx]
            if curr_color == self.GRAY:
                curr_color = self.BLACK
                self.colors[first_elem_indx] = curr_color
            for adjc in g[first_elem_indx]:
                if curr_color == self.BLACK:
                    color_to_be_set = self.WHITE
                else:
                    color_to_be_set = self.BLACK
                if not (self.colors[adjc] == color_to_be_set or self.colors[adjc] == self.GRAY):
                    return False
                self.colors[adjc] = color_to_be_set
                if not visited.get(adjc, False):
                    queue.append(adjc)
            if len(queue) == 0:
                for x in range(len(g)):
                    if not visited.get(x, False):
                        queue.append(x)
                        break
        return True


if __name__ == '__main__':
    print(Solution().isBipartite(
        [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
         [2, 4, 5, 6, 7, 8]]))
