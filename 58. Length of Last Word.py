class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        #Iterate through the string starting from the end
        for char in range(len(s) - 1, -1, -1): 
            if ('A' <= s[char] <= 'Z') or ('a' <= s[char] <= 'z'):
                count += 1
            elif s[char] == ' ' and count > 0:
                return count #Once we loop through the word, return the character count
        return count
    
    #Time complexity: O(n)
    #Memory complexity: O(1)

s = "   fly me   to   the moon  "
my_solution = Solution()
print(my_solution.lengthOfLastWord(s))