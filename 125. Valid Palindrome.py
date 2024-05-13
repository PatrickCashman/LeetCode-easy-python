class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #iterates through the string as a list and checks for alphanumeric characters
        s = [char for char in s if char.isalnum()]
        #returns true or false if the string is a palindrome or not
        return (s == s[::-1])
        #time complexity of O(n)  

s = "A man, a plan, a canal: Panama"
my_solution = Solution()
print(my_solution.isPalindrome(s))