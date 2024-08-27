import itertools

# 31. Coin Sums
# target = 200
# coins = [1, 2, 5, 10, 20, 50, 100, 200]

# ways = [0]*(target+1)
# ways[0] = 1
# for x in coins:
#     for i in range(x, target+1):
#         ways[i] += ways[i-x]

# print(ways[200])


# mat = [[0]*(target+1)]
# mat[0][0] = 1

# for coin in range(1, len(coins)+1):
#     mat.append([0]*(target+1))
#     for x in range(target+1):
#         mat[coin][x] = (mat[coin][x-coins[coin-1]] if x-coins[coin-1] > -1 else 0) + mat[coin-1][x]


# print(mat[-1][-1])
# print(mat[-1][-1] == 73682)
# 32. Pandigital Products
# digits = ["1","2","3","4","5","6","7","8","9"]
# t = set()

# for i in range(1, 5):
#     for option in itertools.permutations(digits, i):
#         for j in range(5-i, 6-i):
#             for num in itertools.permutations(set(digits) - set(option), j):
#                 prod = int(''.join(option)) * int(''.join(num))
#                 if len(option) + len(num) + len(str(prod)) == 9 and digits == sorted(list(option) + list(num) + list(str(prod)[:])):
#                     t.add(prod)
# print(sum(list(t)))