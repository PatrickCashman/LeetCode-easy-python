class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i+1][::-1] + word[i+1:] #returns the word split and reversed at index i + the rest of the word
        return word #if ch is not found return the original
            
my_solution = Solution()
print(my_solution.reversePrefix("abcdef", "d"))