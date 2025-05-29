def knapsack(capacity, items):
    from collections import defaultdict
    memo = defaultdict(int)

    for i in range(len(items) + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                memo[i, j] = 0
                continue
            weight, value = items[i - 1]
            memo[i, j] = memo[i - 1, j]
            if weight <= j:
                memo[i, j] = max(memo[i, j], value + memo[i - 1, j - weight])

    return memo[len(items), capacity]