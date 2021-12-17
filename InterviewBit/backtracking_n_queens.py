class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        fin = []

        def solve(A, res):
            if len(res) == A:
                fin.append(res)
            for i in range(1, A + 1):
                if not self.attack(res, i):
                    solve(A, res + [i])

        solve(A, [])
        return [["." * (i - 1) + "Q" + "." * (A - i) for i in cols] for cols in fin]

    def attack(self, prev, pos):
        for i in range(len(prev)):
            if prev[i] == pos or abs(len(prev) - i) == abs(prev[i] - pos):
                return True
        return False


if __name__ == "__main__":
    s1 = Solution()
    for possible in s1.solveNQueens(4):
        for row in possible:
            print(row)
        print("\n\n")
