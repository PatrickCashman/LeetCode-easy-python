from collections import defaultdict 

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr2_set = set(arr2)
        arr1_count = defaultdict(int)
        end= []
        res = []

        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            arr1_count[n] += 1
        end.sort()

        for n in arr2:
            for _ in range(arr1_count[n]):
                res.append(n)

        return res + end


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

solution = Solution()
print(solution.relativeSortArray(arr1, arr2))