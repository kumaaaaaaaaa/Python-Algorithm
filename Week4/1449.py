n, l = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
cnt = 0
start = 0
for i in a:
    if start<i:
        start = i+l-1
        cnt += 1
print(cnt)