import sys
import copy
from collections import deque

n, m= map(int, sys.stdin.readline().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()
answer = 0


def bfs():
    global answer
    tmp = copy.deepcopy(data)
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                queue.append([i,j])


    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    queue.append([nx,ny])
    cnt = 0
    for i in tmp:
        cnt += i.count(0)
    answer = max(answer,cnt)

def wall(x): 
    if x==3: 
        bfs() 
        return 
    for i in range(n): 
        for j in range(m): 
            if data[i][j]==0: 
                data[i][j]=1 
                wall(x+1) 
                data[i][j]=0 
wall(0) 
print(answer)
