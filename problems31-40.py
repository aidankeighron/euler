# 31. Coin Sums
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

ways = [0]*(target+1)
ways[0] = 1
for x in coins:
    for i in range(x, target+1):
        ways[i] += ways[i-x]

print(ways[200])


mat = [[0]*(target+1)]
mat[0][0] = 1

for coin in range(1, len(coins)+1):
    mat.append([0]*(target+1))
    for x in range(target+1):
        mat[coin][x] = (mat[coin][x-coins[coin-1]] if x-coins[coin-1] > -1 else 0) + mat[coin-1][x]


print(mat[-1][-1])
print(mat[-1][-1] == 73682)