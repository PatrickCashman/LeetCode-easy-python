class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_digits = 0
        
        #Iterate through each digit of the integer n
        while n > 0:
            digit = n % 10 #Extract the last digit
            product *= digit
            sum_digits += digit
            n //= 10 #Remove the last digit from n
        
        return product - sum_digits

    #Time: O(log10(n))
    #Space: O(1)

n = 234
my_solution = Solution()
print(my_solution.subtractProductAndSum(n))