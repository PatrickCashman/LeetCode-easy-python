class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
    
#time: O(log n)
#space: O(1)

nums = [1,3,5,6]
target = 5
my_solution = Solution()
print(my_solution.searchInsert(nums, target))        