class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy = max(candies) 

        return [candy + extraCandies >= max_candy for candy in candies]

        #Time: O(n)
        #Space: O(1)

candies = [2,3,5,1,3]
extraCandies = 3
my_solution = Solution()
print(my_solution.kidsWithCandies(candies, extraCandies))