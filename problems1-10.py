import math
# 1. Multiples of 3 and 5
# print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))
# 2. Even Fibonacci numbers
# def fibonacci(n: int) -> list:
#     if n == 0:
#         return [0]
#     fib = [0, 1]
#     for _ in range(n-1):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# print(sum(fib for fib in fibonacci(33) if fib % 2 == 0))
# 3. Largest prime factor
# print(max(i for i in range(1, int(600851475143**0.5)) if 600851475143 % i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)))))
# 4. Largest palindrome product
# print(max(x*y for x in range(999, 99, -1) for y in range(999, 99, -1) if str(x*y) == str(x*y)[::-1]))
# 5. Smallest multiple
# print(math.lcm(11,12,13,14,15,16,17,18,19,20))
# 6. Sum square difference
# print(sum(i for i in range(1, 101))**2 - sum(i**2 for i in range(1, 101)))
# num = 0
# i = 0
# while num < 10001:
#     i += 1
#     num += int(i > 1 and all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)))
# print(i)
# 8. Largest product in a series
series = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''
series = series.split('\n')


def dfs(point, seen, product, length):
    if length == 13:
        return product
    new_points = []
    seen.add(point)
    
    if point[0] > 0:
        new_points.append((point[0]-1, point[1]))
    if point[1] > 0:
        new_points.append((point[0], point[1]-1))
    if point[0] < len(series)-1:
        new_points.append((point[0]+1, point[1]))
    if point[1] < len(series[0])-1:
        new_points.append((point[0], point[1]+1))
    
    # if point[0] > 0 and point[1] > 0:
    #     new_points.append((point[0]-1, point[1]-1))
    # if point[1] > 0 and point[0] < len(series)-1:
    #     new_points.append((point[0]+1, point[1]-1))
    # if point[0] < len(series)-1 and point[1] < len(series[0])-1:
    #     new_points.append((point[0]+1, point[1]+1))
    # if point[1] < len(series[0])-1 and point[0] > 0:
    #     new_points.append((point[0]-1, point[1]+1))
        
    for new in new_points:
        if new not in seen:
            s = dfs(new, seen, product*int(series[new[0]][new[1]]), length+1)
            return max(product, s or 0)


max_p = 0
for i in range(len(series)):
    for j in range(len(series[i])):
        s = dfs((i, j), set(), int(series[i][j]), 1)
        max_p = max(max_p, s or 0)

print(max_p)