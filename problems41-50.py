from itertools import permutations
# 41. Pandigital Prime
# nums = [int(''.join(p)) for p in permutations('1234567')]
# max_num = 0
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# for num in nums:
#     if is_prime(num):
#         max_num = max(max_num, num)
# print(max_num)
# 42. Coded Triangle Numbers
# print(sum(1 for word in open("./txt/words.txt").read().replace('"', "").split(",") if sum(map(lambda letter: ord(letter) - ord("A") + 1, word)) in [int(0.5 * n * (n + 1)) for n in range(1, 30)]))