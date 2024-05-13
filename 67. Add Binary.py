class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #return bin(int(a, 2) + int(b, 2))[2:]

        #solve without using bin()
        result = ""
        carry = 0
        
        i, j = len(a) - 1, len(b) - 1
        #iterate through both strings
        while i >= 0 or j >= 0 or carry:
            #sum of current digits and carry
            sum_ = carry
            if i >= 0:
                sum_ += int(a[i])
                i -= 1
            if j >= 0:
                sum_ += int(b[j])
                j -= 1
            #append the binary digit to the result
            result = str(sum_ % 2) + result
            carry = sum_ // 2
        return result

#Time: O(n)
#Space O(n)

a = "11"
b = "1"
my_solution = Solution()
print(my_solution.addBinary(a, b))