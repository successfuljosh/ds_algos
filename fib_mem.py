#fibonacci sequence fib(n) =fib(n-1) + fib(n-2)

#complexity of O(2^n)
#python inbuilt cache
from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(n):
    #base case
    if n == 0: return 0
    if n== 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

#optimizing using memoization: this avoid repeatition of calculated data
#memoization stores value to avoid repetition of calculation using a fast table access structure like hash/dict
def fib_mem(n, mem = {}):
    if n in mem:
        return mem[n]
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        mem[n] = fib_mem(n-1) + fib_mem(n-2)
        return mem[n]
n=400
# fib_list = [fibonacci(i) for i in range(n+1)]

fib_list = [fib_mem(i) for i in range(n+1)]
print(fib_list)
# print(mem)