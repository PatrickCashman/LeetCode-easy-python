class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        #runs at a time complexity of O(1)
        if n % 2 == 0:
            return n
        else:
            return n*2 
        

my_solution = Solution()
print(my_solution.smallestEvenMultiple(5))