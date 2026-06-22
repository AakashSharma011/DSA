prices = [7,1,5,3,6,4]

min_price = prices[0]
max_profit = 0

for i in range(1, len(prices)):
    
    profit = prices[i] - min_price
    max_profit = max(max_profit, profit)

    min_price = min(min_price, prices[i])

print(max_profit)