class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function to calculate the greatest common divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Calculate the greatest common divisor of the lengths of the strings
        gcd_len = gcd(len(str1), len(str2))

        # Get the candidate substring which is the prefix of str1 or str2 of length gcd_len
        candidate = str1[:gcd_len]

        # Check if this candidate can construct both str1 and str2 by repeating itself
        if candidate * (len(str1) // gcd_len) == str1 and candidate * (len(str2) // gcd_len) == str2:
            return candidate
        else:
            return ""

#time: O(n + m), where n and m are the lengths of str1 and str1
#space: O(min(n, m))

str1 = "ABABAB"
str2 = "ABAB"
my_solution = Solution()
print(my_solution.gcdOfStrings(str1, str2))