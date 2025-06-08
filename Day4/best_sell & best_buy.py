def maxProfit(prices):
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r 
        r += 1
    return maxP


    maxp = 0
    minbuy = prices[0]

    for num in prices:
        minbuy = min(minbuy, num)
        maxp = max(maxp, num-minbuy)
    return maxp










prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
# Output = 5
# Explanation : Buy on day 2 (price = 1) and sell on day 5(price = 6), profit = 6-1= 5 Not 7-1 = 6, as selling prices needs to be larger than buying prices