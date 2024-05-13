class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        purchase_price = prices[0]
        profit = 0

        for price in prices[1:]: #start loop at index 1 because we have already set our purchase_price to index 0
            if price < purchase_price: #if true, we didn't buy at the lowest price
                purchase_price =  price
            else:
                profit = max(profit, price - purchase_price)

        return profit 
# Time complexity: O(n)
# Space complexity: O(1)

    

prices = [7,1,5,3,6,4]
my_solution = Solution()
print(my_solution.maxProfit(prices))
