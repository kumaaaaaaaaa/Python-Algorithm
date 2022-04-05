n = int(input())
hour = []
cnt = 1
k = 0
for i in range(n):
    start, finish = map(int, input().split())
    hour.append((finish, start))
hour.sort()
for i in range (n-1):
    if hour[i+1][1] >= hour[k][0]:
        cnt += 1
        k = i+1
        
print(cnt)