class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # If needle is an empty string, return -1
            return -1

        # Iterate over possible starting indices in haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Iterate over characters in needle
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    #All characters in needle were successfully matched
                    return i
        # If needle is not found in haystack, return -1
        return -1

#time: O(n + m)
#space: O(m)

haystack = "leetcode"
needle = "leeto"
my_solution = Solution()
print(my_solution.strStr(haystack, needle))               