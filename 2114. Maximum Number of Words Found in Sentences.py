class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0

        for sentence in sentences:
            spaces_count = sentence.count(' ')
            words_count = spaces_count + 1
            max_words = max(max_words, words_count)
        
        return max_words

#Time: O(n*m) n is the number of sentences in the list and m is the length of the sentence
#Space: O(1)

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
my_solution = Solution()
print(my_solution.mostWordsFound(sentences))