import sys

t = int(input())
for i in range(t):
    d = 0
    n = int(input())
    a = list(map(int,sys.stdin.readline().split()))
    a.sort()
    for j in range(2, n):
        d = max(d,abs(a[j]-a[j-2]))
    print(d)
