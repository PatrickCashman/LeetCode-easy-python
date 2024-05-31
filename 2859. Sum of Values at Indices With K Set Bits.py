class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total= 0
        
        for index, num in enumerate(nums):
            if index.bit_count() == k:
                total += num
        return total
    
#Time: O(n*log(index))
#Space: O(1)

nums = [5,10,1,5,2]
k = 1
my_solution = Solution()
print(my_solution.sumIndicesWithKSetBits(nums, k))