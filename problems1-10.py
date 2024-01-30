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