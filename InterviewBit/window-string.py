from collections import deque


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, s, t):
        if not s or not t:
            return ''
        required_chars = {}
        for b in t:
            if b not in required_chars:
                required_chars[b] = deque()
            required_chars[b].append(-1)
        n_needed = len(t)
        best = None
        cur_min = None
        for idx, a in enumerate(s):
            if a in required_chars:
                old_idx = required_chars[a].popleft()
                required_chars[a].append(idx)
                if n_needed != 0 and old_idx == -1:
                    n_needed -= 1
                if n_needed == 0 and (cur_min is None or old_idx == cur_min):
                    cur_min = min([a[0] for a in required_chars.values()])
                    if best is None or best[1] - best[0] > idx - cur_min:
                        best = [cur_min, idx]
        if best is None:
            return ''
        return s[best[0]:best[1] + 1]


if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.minWindow("ADOBECODEBANC", "ADBC"))
