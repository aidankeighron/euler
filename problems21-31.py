import math, time
# 21. Amicable Numbers
# print(sum(i for i in range(10000+1) if (d := lambda n: sum(j+n//j for j in range(2, int(math.sqrt(n))+1) if n % j == 0)+1)(1) and i == d(d(i)) and i != d(i)))
# 22. Names Scores
# print(sum(sum(ord(ch) - ord('A') + 1 for ch in name) * (i+1) for i, name in enumerate(sorted([line.split(",") for line in open('./txt/names.txt')][0]))))