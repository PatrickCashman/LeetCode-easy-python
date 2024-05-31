class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = [] #More efficent to add charcters to array and change to a string
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            #Append charcters to our array
            merged.append(word1[i])
            merged.append(word2[j])
            #Increment pointers
            i += 1
            j += 1

        #Append any charcters that are left over after one of our strings runs out of characters
        merged.append(word1[i:])
        merged.append(word2[j:])
        #return the array as a string
        return "".join(merged)

#time and space: O(n+m)

word1 = "abc"
word2 = "pqr"
my_solution = Solution()
print(my_solution.mergeAlternately(word1, word2))