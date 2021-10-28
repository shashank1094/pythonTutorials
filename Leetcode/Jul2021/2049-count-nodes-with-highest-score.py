from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        from collections import defaultdict, Counter
        graph = defaultdict(list)
        for _node, parent in enumerate(parents):
            graph[parent].append(_node)
        # print(graph)
        counter = Counter()
        n = len(parents)

        def count_nodes(node):
            score = 1
            children = 0
            for child in graph[node]:
                t = count_nodes(child)
                t += 1
                children += t
                score = score * t
            upward_nodes = n - 1 - children
            # print(locals())
            if upward_nodes:
                score = score * upward_nodes
            counter[score] += 1
            return children

        count_nodes(0)
        return counter[max(counter.keys())]


if __name__ == '__main__':
    print(Solution().countHighestScoreNodes([-1, 2, 0, 2, 0]))
