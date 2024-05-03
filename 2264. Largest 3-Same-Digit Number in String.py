class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_num = ''
        for i in range(len(num) - 2): #iterate of the substring with a length of 3
            substring = num[i:i+3] #get the substring of length 3 starting at index i
            if len(set(substring)) == 1: #check if the substring is just one unique digit
                if substring > good_num:
                    good_num = substring 
        return good_num #returns the maximum good integer
    
my_solution =Solution()
print(my_solution.largestGoodInteger("6777133339"))
