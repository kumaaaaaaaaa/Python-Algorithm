import sys
import copy
from collections import deque

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
op = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9
def dfs(i, total, add, sub, mul, div):
    global maximum, minimum
    if i == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if add:
        dfs(i+1, total + data[i], add -1, sub, mul, div)
    if sub:
        dfs(i+1, total - data[i], add , sub -1, mul, div)
    if mul:
        dfs(i+1, total * data[i], add , sub, mul -1, div)
    if div:
        dfs(i+1, int(total / data[i]), add , sub, mul, div -1)
    
dfs(1,data[0],op[0],op[1],op[2],op[3])
print(maximum)
print(minimum)