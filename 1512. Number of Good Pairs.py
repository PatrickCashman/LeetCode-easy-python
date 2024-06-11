class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        freq = {}
        
        for num in nums:
            if num in freq:
                # Add the current frequency to the count
                count += freq[num]  
                # Increment the frequency of the number
                freq[num] += 1      
            else:
                # Initialize the frequency if the number is seen for the first time
                freq[num] = 1       
            
        return count

# Time: O(n)
# Space: O(n)

nums = [1,2,3,1,1,3]
solution_instance = Solution()
print(solution_instance.numIdenticalPairs(nums))

