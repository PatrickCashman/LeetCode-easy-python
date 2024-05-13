class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left_pointer = 1

        for right_pointer in range(1, len(nums)):
            #check if the value at our right_pointer is new or a value we've seen before
            if nums[right_pointer] != nums[right_pointer - 1]:
                #if they are not the same, it is a new value and should be in our array
                nums[left_pointer] = nums[right_pointer] 
                left_pointer += 1
        return left_pointer #returns at O(n) time complexity
    

nums = [1,1,2]
my_solution = Solution()
print(my_solution.removeDuplicates(nums))