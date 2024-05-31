class Solution:
    def interpret(self, command: str) -> str:
        result = ''

        for i in range(len(command)):
            if command[i] == "G":
                result += "G"
            if command[i] == "(" and command[i+1] == ")":
                result += "o"
            if command[i] == "a" and command[i+1] == "l":
                result += "al"
        return result
    
#Time: O(n)
#Space: O(n)  

command = "G()()()()(al)"
my_solution = Solution()
print(my_solution.interpret(command))