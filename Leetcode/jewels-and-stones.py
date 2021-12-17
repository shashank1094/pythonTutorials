class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {x: True for x in J}
        result = [y for y in S if jewels.get(y)]
        return len(result)
