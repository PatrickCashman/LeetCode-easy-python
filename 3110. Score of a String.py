class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        #iterate over the string to get the index and value of each character
        for i in range(len(s) - 1):
            ascii_value1 = ord(s[i]) #get the ASCII values
            ascii_value2 = ord(s[i + 1])
            difference = abs(ascii_value1 - ascii_value2)
            score += difference
        return score

my_solution = Solution()
print(my_solution.scoreOfString("hello"))