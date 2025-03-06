# https://leetcode.com/discuss/interview-experience/1470686/amazon-online-assessment
from functools import cache


def findValidDiscountCoupons(discounts):
    true = 1
    false = 0

    @cache
    def dp(discount):
        if not discount:
            return true

        n = len(discount)
        if n == 1:
            return false

        if discount[0] == discount[n - 1]:
            return dp(discount[1:n-1])
        elif dp(discount[:n//2]) and dp(discount[n//2:]):
            return true
        return false

    def func(discount):
        if len(discount) % 2:
            return false
        return dp(discount)

    return list(map(func, discounts))

print(findValidDiscountCoupons(["abba", "abca", "aca", "daabbd"]))