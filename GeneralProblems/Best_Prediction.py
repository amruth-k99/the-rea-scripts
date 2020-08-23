n = 4
k = 2
a = 100
price = [20, 10, 30, 40]
profit_perc = [5, 10, 30, 40]
dis = dict(zip(price, profit_perc))
final_profit = 0
temp_val = 50
for x in range(1, n+1):
    amount = a
    attempts = 2
    prices = price.sort()
    tmp_money = 100
    tmp_profit = 0
    while tmp_money:
        for y in range(x):
            tmp_money = tmp_money-prices[0]
            tmp_profit = tmp_profit+(dis[prices[0]])*prices[0]/100
    if(tmp_profit > final):
        final = tmp_profit
print()
