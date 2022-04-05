import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if(num == 0):
        if(len(heap) == 0):
            print("0")
            continue
        result = heapq.heappop(heap)
        result = -result
        print(result)
    else:
        heapq.heappush(heap, -num)