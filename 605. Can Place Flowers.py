class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Pad the array with empty plots at both ends to handle edge cases
        flower = [0] + flowerbed + [0]

        # Iterate through the flowerbed from the first to the last real plot
        for i in range(1, len(flower) - 1):
            # Check if the current, previous, and next plots are empty
            if flower[i-1] == 0 and flower[i] == 0 and flower[i+1] == 0:
                # Plant a flower at the current plot
                flower[i] = 1
                # Decrement n as we have planted one flower
                n -= 1
                # If all required flowers are planted, return True
                if n == 0:
                    return True

        # If we have not been able to plant all flowers, return whether n is less than or equal to 0
        return n <= 0
    
#time: O(m), where m is the length of the original flowerbed array
#space: O(m)

flowerbed = [1,0,0,0,1]
n = 1
my_solution = Solution()
print(my_solution.canPlaceFlowers(flowerbed, n))