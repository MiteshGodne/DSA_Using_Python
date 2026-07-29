'''You are given an array prices where prices[sell] is the price of a given stock on the ith day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxi = 0
        buy = 0
        cdiff = 0
        for sell in range(1, len(prices)):
            cdiff = prices[sell] - prices[buy]
            if cdiff > maxi:
                maxi = cdiff
            if cdiff < 0:
                buy = sell
        return maxi
        
if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,5,7,0,4]
    print(obj.maxProfit(nums))