import math
# 21. Amicable Numbers
# print(sum(i for i in range(10000+1) if (d := lambda n: sum(j+n//j for j in range(2, int(math.sqrt(n))+1) if n % j == 0)+1)(1) and i == d(d(i)) and i != d(i)))