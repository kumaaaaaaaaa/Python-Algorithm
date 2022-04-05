n, k = map(int, input().split())
cnt = 0
coin = []
for i in range(n):
    coin.insert(0,int(input()))
for i in coin:
    cnt += k // i
    k %= i
print(cnt)