class Solution:
    def makeGood(self, s: str) -> str:
        result = '' #empty string to store the 'good' string
        for i in s:
            #check if result is not empty and if the characters have opposite cese
            if result and i.swapcase() == result[-1]:
                result = result[:-1] #remove last character from result
            else: #if condition isn't met append the current charcter
                result += i
        return result
    
my_solution = Solution()
print(my_solution.makeGood("leEeetcode"))