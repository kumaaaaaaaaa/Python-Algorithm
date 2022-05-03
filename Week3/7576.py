import sys
from collections import deque

l = []
m, n= map(int, sys.stdin.readline().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

data = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m:
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y]+1
                    queue.append((nx,ny))
            

for j in range(n):
    for k in range(m):
        if data[j][k] == 1:
            queue.append((j,k))
bfs()
flag = 0
result = -2

for j in range(n):
    for k in range(m):
        if data[j][k] == 0:
            flag = 1
        result = max(result,data[j][k])
if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)