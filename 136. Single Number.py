class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0  # Initialize result to 0. XOR with 0 does not change the number.

        # Iterate over each number in the list.
        for n in nums:
            result = n ^ result  # XOR the current number with the result.
            # The XOR operation will cancel out numbers appearing in pairs, leaving the single number.

        return result  # After the loop, result will be the number that appears only once.

#time: O(n)
#space: O(1)

nums = [4,1,2,1,2]
solution_instance = Solution()
print(solution_instance.singleNumber(nums))