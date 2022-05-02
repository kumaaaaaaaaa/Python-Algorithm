import sys

t = int(sys.stdin.readline())
for i in range(t):
    a, b= map(int, sys.stdin.readline().split())
    al = list(map(int, sys.stdin.readline().split()))
    bl = list(map(int, sys.stdin.readline().split()))
    al.sort()
    bl.sort()
    start = 0
    cnt = 0
 
    for j in range(a):
        while True:
            if start==b or al[j]<=bl[start]:
                cnt+=start
                break
            else:   
                start+=1
                
    print(cnt)