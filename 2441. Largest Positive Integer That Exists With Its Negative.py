class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums = sorted(nums, key = lambda x: (abs(x), x), reverse = True)
        #sort the list in absolute decending order
        for i in range(len(nums) - 1):
            if abs(nums[i]) == abs(nums[i+1]) and (nums[i] + nums[i+1]) == 0:
                #compare the values and make sure they aren't duplicates
                return abs(nums[i])          
        return -1


solution_instance = Solution()
print(solution_instance.findMaxK([-9,-43,24,-23,-16,-30,-38,-30]))