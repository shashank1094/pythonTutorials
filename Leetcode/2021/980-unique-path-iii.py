from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # first, prepare the starting and ending points
        # simultaneously, record all the non-obstacle coordinates
        start = end = None
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visit.add((i, j))
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                    visit.add((i, j))
        qwerty = 0

        def backtrack(x, y, visit):
            if (x, y) == end:
                # implement success condition: valid only if there are no more coordinates to visit
                return len(visit) == 0
            result = 0  # assume no valid paths by default

            # we need to try every possible path from this coordinate
            if (x - 1, y) in visit:
                # the coordinate directly above this one is non-obstacle, try that path
                visit.remove((x - 1, y))  # first, note down the 'visited status' of the coordinate
                result += backtrack(x - 1, y, visit)  # then, DFS to find all valid paths from that coordinate
                visit.add((x - 1, y))  # last, reset the 'visited status' of the coordinate
            if (x + 1, y) in visit:
                # the coordinate directly below this one is non-obstacle, try that path
                visit.remove((x + 1, y))
                result += backtrack(x + 1, y, visit)
                visit.add((x + 1, y))
            if (x, y - 1) in visit:
                # the coordinate directly to the left of this one is non-obstacle, try that path
                visit.remove((x, y - 1))
                result += backtrack(x, y - 1, visit)
                visit.add((x, y - 1))
            if (x, y + 1) in visit:
                # the coordinate directly to the right of this one is non-obstacle, try that path
                visit.remove((x, y + 1))
                result += backtrack(x, y + 1, visit)
                visit.add((x, y + 1))
            return result

        return backtrack(start[0], start[1],
                         visit)  # we start from the starting point, backtrack all the way back, and consolidate the result


if __name__ == '__main__':
    print(Solution().uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
