def buy_and_sell_twice(prices):
    l = [0] * len(prices)   #l represents max profit at day i after buy/sell once
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
        l[i] = max_profit
    
    max2 = float('-inf')
    for i in reversed(range(1, len(prices))):
        max2 = max(max2, prices[i])
        max_profit = max(max_profit, max2 - prices[i] + l[i - 1])

    return max_profit
