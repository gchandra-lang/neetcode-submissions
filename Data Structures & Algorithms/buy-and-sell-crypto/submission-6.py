class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        potentialProfit = [0]  
        length = len(prices)
        l = 0
        r = 1
        
        while r < length:  
            diff = prices[r] - prices[l]
            
            if diff < 0:
                l = r  
            else:
                potentialProfit.append(diff)
            
            r += 1 
            
        return max(potentialProfit)