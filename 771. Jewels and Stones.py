class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel_set = set(jewels)
        #using a set is much faster run time, in comparison to searching through the jewels string
        for stone in stones:
            if stone in jewel_set:
                count += 1

        return count

#Time: O(n + m) n is the length of jewels and m is the length of stones
#Space: O(n)

jewels = "aA"
stones = "aAAbbbb"
my_solution = Solution()
print(my_solution.numJewelsInStones(jewels, stones))