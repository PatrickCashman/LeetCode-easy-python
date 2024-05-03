class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {} #store elements of nums with their indices

        for i, j in enumerate(nums): #provides index i and value j of each element
            dif = target - j
            if dif in hashmap: #check if the difference exists in our dictionary
                return[hashmap[dif], i]
            hashmap[j] = i #if difference is not found, store current element j with index i
            
nums = [2, 7, 11, 15]
target = 9

solution_instance = Solution()
print(solution_instance.twoSum(nums, target))