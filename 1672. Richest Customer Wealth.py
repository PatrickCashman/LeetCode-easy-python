class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(wealth) for wealth in accounts])
    #calculates the sum of each sublist and returns the max value
    #returns in O(m x n) complexity.


accounts = [[2,8,7],[7,1,3],[1,9,5]]
my_solution = Solution()
print(my_solution.maximumWealth(accounts))