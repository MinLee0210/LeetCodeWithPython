def maxProfit(prices):
    for price in prices:
        lower_bound = min(prices)
        upper_bound = max(prices)
        
        if (price == lower_bound) and prices.index(price) >= prices.index(lower_bound) and prices.index(upper_bound):
            
        
        
list = [7, 1, 5, 3, 6, 4]
# print(maxProfit(list))

