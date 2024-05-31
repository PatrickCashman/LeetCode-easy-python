class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place the non-val element at the position of the k pointer
                k += 1  # Move the k pointer to the next position

        return k

#time: O(n)
#space: O(1)

nums = [3,2,2,3]
val = 3
my_solution = Solution()
print(my_solution.removeElement(nums, val))

