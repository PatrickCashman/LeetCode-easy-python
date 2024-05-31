class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        # Loop until we reach the end of either string s or string t
        while i < len(s) and j < len(t):
        # If characters at i in s and j in t match, move pointer i to the next character in s
            if s[i] == t[j]:
                # By incrementing i only when there is a match ensures that we find characters in the correct order of s
                i += 1
            j += 1
        # If i has reached the end of s, it means all characters in s have been found in t in order
        return True if i == len(s) else False
    
#time: O(n + m)

s = "abc"
t = "ahbgdc"
my_solution = Solution()
print(my_solution.isSubsequence(s, t))       