import heapq
import sys

heap = []
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])

arr.sort()
for i in range(n): 
    if len(heap) != 0 and heap[0] <= arr[i][0]: 
        heapq.heappop(heap) 
    heapq.heappush(heap,arr[i][1])
print(len(heap))