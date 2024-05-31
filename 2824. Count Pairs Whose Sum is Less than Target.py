class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right =  n -1
        count = 0

        while left < right:
            if (nums[left] + nums[right]) < target:
                #If the sum is less than target, then all elements between left and right
                #form valid pairs with nums[left]
                #Increment count by the number of such valid pairs
                count += right - left
                left += 1
                #Move the left pointer to the right to explore more pairs
            else:
                right -= 1 
            #If the sum is not less than target, move the right pointer to the left

        return count

#Time O(n log n)
#Space O(1)

nums = [-1,1,2,3,1]
target = 2
my_solution = Solution()
print(my_solution.countPairs(nums, target))