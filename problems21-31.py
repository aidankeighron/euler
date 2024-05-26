import math, time, itertools
from decimal import Decimal, getcontext
# 21. Amicable Numbers
# print(sum(i for i in range(10000+1) if (d := lambda n: sum(j+n//j for j in range(2, int(math.sqrt(n))+1) if n % j == 0)+1)(1) and i == d(d(i)) and i != d(i)))
# 22. Names Scores
# print(sum(sum(ord(ch) - ord('A') + 1 for ch in name) * (i+1) for i, name in enumerate(sorted([line.split(",") for line in open('./txt/names.txt')][0]))))
# 23. Non-Abundant Sums
# abundant = [target for target in range(12, 28123) if sum(f+target//f + (-f if f == math.sqrt(target) else 0) for f in range(2, int(math.sqrt(target))+1) if target % f == 0) > target]
# nums = list(range(1, 28123+1))
# for i, num in enumerate(abundant):
#     for other in abundant[i:]:
#         if num+other <= 28123:
#             nums[num+other-1] = 0
# print(sum(nums))
# print(sum(nums) == 4179871)
# 24. Lexicographic Permutations
# print(sorted([''.join(perm) for perm in itertools.permutations(["0","1","2","3","4","5","6","7","8","9"])])[1_000_000-1])
# 25. Fibonacci Number
# def fib():
#     a, b = 0, 1
#     while True:
#         yield b
#         a, b = b, a+b

# f, x = enumerate(fib()), 0
# while len(str(x)) < 1000:
#     i, x = next(f)
# print(i+1)
# 26. Reciprocal Cycles
# getcontext().prec = 5000
# out = 0
# for i in range(1, 1000+1):
#     number, j = str(Decimal(1)/Decimal(i))[2:], 3
#     while j < 1000:
#         if 3*j > len(number):
#             break
#         if number[:j] == number[j:2*j] and number[:j] == number[2*j:3*j]:
#             out = max(out, j)
#             break
#         j += 1
# print(out+1)