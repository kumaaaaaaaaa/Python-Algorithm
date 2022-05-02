import sys

t = int(input())
for i in range(t):
    cnt = 1
    a = []
    n = int(input())
    for i in range(n):
        x, y = map(int,sys.stdin.readline().split())
        a.append([x, y])
    a.sort()
    max = a[0][1]
    for i in range(1,n):
        if max > a[i][1]:
            cnt += 1
            max = a[i][1]
    print(cnt)