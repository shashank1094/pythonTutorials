# https://leetcode.com/problems/super-pow/


class Solution:

    def superPow(self, a, b):
        self.dp = {}
        result = 1
        for digit in b:
            result = self.util(result, 10, 1337) * self.util(a, digit, 1337) % 1337
        return result

    # def superPow(self, a, b):
    #     temp_b = self.get_number_to_be_raised(b)
    #     self.dp = {}
    #     return self.util(a, temp_b)

    def util(self, a, b, base):
        if (a, b) in self.dp:
            return self.dp[(a, b)]
        if b == 0:
            return 1
        if b == 1:
            return a
        if b % 2 == 0:
            temp = self.util(a, b // 2, base)
            ans = ((temp % base) * (temp % base)) % base
            self.dp[(a, b)] = ans
            return ans
        else:
            temp_1 = (self.util(a, b // 2, base))
            temp_2 = (self.util(a, (b // 2) + 1, base))
            ans = ((temp_1 % base) * (temp_2 % base)) % base
            self.dp[(a, b)] = ans
            return ans

    @staticmethod
    def get_number_to_be_raised(b):
        ans = 0
        for x in range(len(b)):
            ans += (10 ** x) * b[~x]
        return ans


if __name__ == '__main__':
    print(Solution().superPow(2, [1, 0, 1]))
