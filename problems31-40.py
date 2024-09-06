import itertools
from functools import reduce
from operator import mul
import math
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
# 33. Digit Cancelling Fractions
# numerator = 1
# dominator = 1

# for i in range(10, 100):
#     for j in range(10, 100):
#         if i == j or i/j > 1 or str(i)[-1] == '0' and str(j)[-1] == '0':
#             continue
#         for num in str(i):
#             for num1 in str(j):
#                 if num == num1:
#                     new_i = int(str(i).replace(str(num), '', 1))
#                     new_j = int(str(j).replace(str(num1), '', 1))
#                     if not new_i or not new_j:
#                         continue
#                     if i/j == new_i/new_j:
#                         numerator *= i
#                         dominator *= j

# print(dominator // math.gcd(numerator, dominator))
# 34. Digit Factorials
# print(sum(i for i in range(3, 100000) if sum(reduce(mul, range(1,int(d)+1), 1) for d in str(i)[:]) == i))
