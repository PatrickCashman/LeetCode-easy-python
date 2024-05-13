class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1  #carry as 1 to represent adding one

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry  
            digits[i] = total % 10  #extracts the least significant digit from the total
            carry = total // 10 #quotient represents the carry-over to the next digit position

        # If there is still a carry after the loop, prepend it to the digits
        if carry:
            digits.insert(0, carry)

        return digits
        #Time complexity: O(n)
        #Memory complexity: O(1)


digits = [4,3,2,1]
my_solution = Solution()
print(my_solution.plusOne(digits))