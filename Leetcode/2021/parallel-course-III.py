# https://leetcode.com/problems/parallel-courses-iii/

from collections import deque
from collections import defaultdict
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        edges = defaultdict(list)
        indegrees = [0] * n
        for relation in relations:
            edges[relation[0] - 1].append(relation[1] - 1)
            indegrees[relation[1] - 1] += 1

        # Initializing a queue
        q = deque()
        for indx, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(indx)
            else:
                pass

        distance = [0] * n
        # print(q, time, edges, indegrees)
        while q:
            # print(q, time, edges, indegrees, distance)
            node = q.popleft()
            node_dist = max(distance[node], time[node])
            distance[node] = node_dist
            if node in edges:
                for neigbour in edges[node]:
                    indegrees[neigbour] -= 1
                    distance[neigbour] = max(distance[node] + time[neigbour], distance[neigbour])
                    if indegrees[neigbour] == 0:
                        q.append(neigbour)

        return max(distance)


print(Solution().minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
# print(Solution().minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
