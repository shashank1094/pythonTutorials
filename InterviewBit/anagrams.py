class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        ans = []
        memo = {}
        for index, item in enumerate(A):
            req_item = ''.join(sorted(item))
            if req_item in memo:
                memo[req_item].append(index+1)
            else:
                memo[req_item] = [index + 1]
        for key, value in memo.items():
            ans.append(value)
        ans.sort()
        return ans


if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.anagrams(["cat", "dog", "god", "crow", "odg", 'tca']))
