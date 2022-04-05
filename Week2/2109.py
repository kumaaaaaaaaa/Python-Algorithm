import sys
import heapq

n = int(sys.stdin.readline())
p = []
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])

arr.sort(key = lambda x:x[1])
for i in range(n):
    heapq.heappush(p,arr[i][0])
    if len(p)>arr[i][1]:
        heapq.heappop(p)
print(sum(p))