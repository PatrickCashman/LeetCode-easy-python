class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the number of ways to reach the first and second steps
        previous, current = 1, 1
    
        # Compute the number of ways to reach each step from 2 to n
        # Loop from index 2 to n inclusive because we already have the amount of steps for index 0 and 1
        for step in range(2, n + 1):
            # The number of ways to reach the current step is the sum of the ways to reach the two preceding steps
            next_step = previous + current      
            # Update the variables for the next iteration
            previous = current
            current = next_step
    
        # The final number of ways to reach the n-th step
        return current

#time: O(n)
#space: O(1)

n = 3
my_solution = Solution()
print(my_solution.climbStairs(n))       