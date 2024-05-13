class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if nums[mid] > target: #if our target is greater than our mid point we must move our right pointer to the left
                right_pointer = mid - 1
            elif nums[mid] < target: #if our target is less than our mid point we must move our left pointer to the right
                left_pointer = mid + 1
            else: 
                return mid
        return -1 #returns in O(log n)
    

nums = [-1,0,3,5,9,12]
target = 9
my_solution = Solution()
print(my_solution.search(nums, target))