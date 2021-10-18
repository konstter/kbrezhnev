# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def maxprofit(prices):
    l = len(prices)
    if l <= 1: return 0
    profit = prices[1] - prices[0]
    minimum = prices[0]

    for i in range(1, l):
        if prices[i] - minimum > profit:
            profit = prices[i] - minimum
        if prices[i] < minimum:
            minimum = prices[i]

    if profit < 0: return 0
    return profit

if __name__ == '__main__':
    print(maxprofit([7,6,5,4,3,2]))
    # print(maxprofit([7,1,5,3,6,4]))

