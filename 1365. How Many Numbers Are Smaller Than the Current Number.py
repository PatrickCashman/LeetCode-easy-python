class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count = [0] * 101 #Constraint: 0 <= nums[i] <= 100
        for num in nums:
            count[num] += 1 #Counting the occurrences of each number
        
        for i in range(1, len(count)):
            count[i] += count[i - 1] #Update each count to be the sum of all previous counts
        
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(count[num - 1]) #Count of numbers smaller than num is count[num - 1]
        
        return result

    #Time: O(n)
    #Space: O(n)

nums = [8,1,2,2,3]
my_solution = Solution()
print(my_solution.smallerNumbersThanCurrent(nums))