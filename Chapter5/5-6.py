def buy_and_sell_stock_once(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit

print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
