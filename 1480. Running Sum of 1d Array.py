class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = [nums[0]]

        for i in range(1, len(nums)):
            running_sum.append(running_sum[-1] + nums[i])

        return running_sum

#Time: O(n)
#Space: O(n)

nums = [3,1,2,10,1]
my_solution = Solution()
print(my_solution.runningSum(nums))