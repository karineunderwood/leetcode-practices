class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        """This function initialises two pointers, left and right, and max_proft at 0. Whilst
        the right pointer is smaller than the length of prices, if prices[l] < prices[r] 
        (the trade is profitable), the profit is calculated, and the max of max_profit and 
        profit is assigned as max_profit. Otherwise, the left pointer is updated to the 
        position of the right pointer, and the right pointer is incremented to the right."""
        
        left = 0
        right = 1
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                print(profit)
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit
                
        
        
        
        
        
                    
                    
            
        
        
        