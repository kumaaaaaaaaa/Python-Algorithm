def change(a):
    if i == n-1:
        a[i] = 1-a[i]
        a[i-1] = 1-a[i-1]
    else:
        a[i] = 1-a[i]
        a[i-1] = 1-a[i-1]
        a[i+1] = 1-a[i+1]

n = int(input())
cnt1 = 1
cnt2 = 0
a = list(map(int,input()))
a2 = a.copy()
b = list(map(int,input()))

a[0] = 1-a[0]
a[1] = 1-a[1]

for i in range(1,n):
    if a[i-1] != b[i-1]:
        change(a)
        cnt1+=1
if a != b:
    cnt1 = -1

for i in range(1,n):
    if a2[i-1] != b[i-1]:
        change(a2)
        cnt2+=1
if a2 != b:
    cnt2 = -1

if cnt1 >= 0 and cnt2 >= 0:
    print(min(cnt1,cnt2))
elif cnt1>=0 and cnt2 < 0:
    print(cnt1)
elif cnt1<0 and cnt2>=0:
    print(cnt2)
else:
    print(-1)
