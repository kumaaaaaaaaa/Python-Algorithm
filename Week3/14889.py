import sys
from collections import deque

def member(num, k):
    global minimum
    if num == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += data[i][j]
                elif not visited[i] and not visited[j]:
                    link += data[i][j]
        minimum = min(minimum, abs(link - start))
        return 
    for i in range(k, n):
        if not visited[i]:
            visited[i] = True
            member(num+1, i+1)
            visited[i] = False


n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
minimum = 1e9

member(0, 0)
print(minimum)