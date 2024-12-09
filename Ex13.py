def knapSack(capacity, wt, profit):

    elements = len(wt)
    dp = [0 for _ in range(capacity + 1)]

    for i in range(1, elements + 1):
        for w in range(capacity, 0, -1):
            if wt[i - 1] <= w:
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + profit[i - 1])

    return dp[capacity]

profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
print(knapSack(capacity, weight, profit))

