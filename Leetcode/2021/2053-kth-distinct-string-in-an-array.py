from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import defaultdict
        counter = defaultdict(int)
        for element in arr:
            counter[element] += 1
        i = 0
        print(counter)
        for _key, _val in counter.items():
            if _val == 1:
                i += 1
                if i == k:
                    return _key
        return None


if __name__ == '__main__':
    print(Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
