class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = { ")" : "(", "]" : "[", "}" : "{" }
        #allows us to check for matching pairs
        
        for i in s:
            if i in close_open:
                if stack and stack[-1] == close_open[i]:
                    #if the charater matches and has a pair in the hashmap we can pop
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
    
        return True if not stack else False
        #if the stack is empty we can return true
    
s = "(]"
my_solution = Solution()
print(my_solution.isValid(s))