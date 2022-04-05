n = int(input())
s = []
o = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        o.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        o.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in o:
        print(i)