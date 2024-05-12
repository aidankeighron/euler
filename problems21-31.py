import math, time
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