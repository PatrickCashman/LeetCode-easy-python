class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort() #sorts the array for comparison

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]: #compare for duplicates
                return True          
        return False


solution_instance = Solution()
print(solution_instance.containsDuplicate([2,14,18,22,22]))