class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort() #sort in ascending order

        if(prices[0] + prices[1]) <= money: #check the sum of the lowest priced chocolate
            return (money - (prices[0] + prices[1])) #buy the lowest priced chocolate
                
        return money #if you can't buy the two lowest, you can't buy anything


my_solution = Solution()
print(my_solution.buyChoco([98,54,6,34,66,63,52,39], 62))
