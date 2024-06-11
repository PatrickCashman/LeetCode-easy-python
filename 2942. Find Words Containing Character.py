class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        result = []

        # Iterate over each word in the list with its index
        for index, word in enumerate(words):
            if x in word:
                result.append(index)  
        # Return the list of indices
        return result 

# Time: O(n * m)
# Space: O(k)

words = ["leet","code"]
x = "e"
solution_instance = Solution()
print(solution_instance.findWordsContaining(words, x))