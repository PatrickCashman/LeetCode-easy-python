from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #if string aren't the same length they can't be anagrams
            return False

        return Counter(s) == Counter(t)
        #compares the count of the characters for each string

solution_instance = Solution()
print(solution_instance.isAnagram("anagram", "nagaram"))