def maximizeCoins(coins):
    max_x = max_y = 0
    for coin in coins:
        max_x = max(coin[0]+1, max_x)
        max_y = max(coin[1]+1, y)
    matrix = [[0 for j in range(y)] for i in range(max_x)]
    for coin in coins:
        matrix[coin[0]][coin[1]] += 1
    for i in range(max_x):
        for j in range(max_y):
            if i == j == 0:
                continue
            if not i:
                matrix[i][j] += matrix[i][j-1]
            elif not j:
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += max(matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]
