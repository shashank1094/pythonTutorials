class Solution:
    def convertToBase7(self, num: int) -> str:
        # Store each digit in array as we iterate
        s = []
        # Base case where while loop never runs
        if num == 0:
            return "0"
        # If num is negative, make it positive so the calculation is easier
        # Add a boolean flag
        negative_flag = False
        if num < 0:
            negative_flag = True
            num = -num
        # While our division (into base 7) requires more steps to finish adding digits
        while num > 0:
            # Append the next digit to the array
            # This begins from the smallest digit (rightmost)
            # Thus, we must reverse the string after we finish
            # (Last computation => Largest digit)
            s.append(str(num % 7))
            # Perform the actual division by our base, 7, on num
            num //= 7

        # If it is negative add a '-', then join into a string and return
        # Again, s is reversed in order to place larger digits first
        return ('-' if negative_flag else '') + ''.join(s[::-1])

if __name__ == '__main__':
    print(Solution().convertToBase7(100))
    print(Solution().convertToBase7(-7))