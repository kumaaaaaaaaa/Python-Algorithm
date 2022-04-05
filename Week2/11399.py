n = int(input())
tmp = 0
sum = 0
p = [int(i) for i in input().split()]
p.sort()

for i in range(n):
    sum += tmp + p[i]
    tmp += p[i]
print(sum)