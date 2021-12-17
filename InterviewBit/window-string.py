# from collections import deque
#
#
# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return a strings
#     def minWindow(self, s, t):
#         if not s or not t:
#             return ''
#         required_chars = {}
#         for b in t:
#             if b not in required_chars:
#                 required_chars[b] = deque()
#             required_chars[b].append(-1)
#         n_needed = len(t)
#         best = None
#         cur_min = None
#         for idx, a in enumerate(s):
#             if a in required_chars:
#                 old_idx = required_chars[a].popleft()
#                 required_chars[a].append(idx)
#                 if n_needed != 0 and old_idx == -1:
#                     n_needed -= 1
#                 if n_needed == 0 and (cur_min is None or old_idx == cur_min):
#                     cur_min = min([a[0] for a in required_chars.values()])
#                     if best is None or best[1] - best[0] > idx - cur_min:
#                         best = [cur_min, idx]
#         if best is None:
#             return ''
#         return s[best[0]:best[1] + 1]
class Solution:
    # @param S : string
    # @param T : string
    # @return a string
    def minWindow(self, S, T):
        start = 0
        end = 0
        need = {}
        window = ""
        for s in T:
            if s not in need:
                need[s] = -1
            else:
                need[s] -= 1

        while end < len(S):
            char = S[end]
            if char in need:
                need[char] += 1
            end += 1

            while len([i for i in need.values() if i < 0]) == 0:
                # this is a valid window
                # we can advance start
                if window == "" or (end - start) < len(window):
                    window = S[start:end]

                if S[start] not in need or need[S[start]] > 0:
                    if S[start] in need:
                        need[S[start]] -= 1
                    start += 1
                else:
                    break

        return window


if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.minWindow("ADOBECODEBANC", "ADBC"))
