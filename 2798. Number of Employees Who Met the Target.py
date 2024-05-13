class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1

        return count #returns in O(n) time complexity
    

hours = [0,1,2,3,4]
target = 3
my_solution = Solution()
print(my_solution.numberOfEmployeesWhoMetTarget(hours, target))
