#import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
gg = []

#틀린 답(모래시계X)
for i in range(n):
    gg.append(list(map(int, input().split())))

m = int(input())

for i in range(m):
    a, b, c = map(int, input().split())

    if b == 0:
        temp = gg[a-1][c:]+gg[a-1][:c]
        gg[a-1] = temp

    else:
        temp = gg[a - 1][-c:] + gg[a - 1][:-c]
        gg[a - 1] = temp

cnt = 0
for i in range(n):
    gg[i][i//2]


# 시뮬레이션(모레시계 회전) 구현
'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    
    if t == 0: #왼쪽
        for _ in range(k): #c만큼
            a[h-1].append(a[h-1].pop(0)) #회전
            
    else: #오른쪽
        for _ in range(k): #c만큼
            a[h-1].insert(0, a[h-1].pop()) #회전

s = 0
e = n-1
res = 0

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    
    if i < n//2: #좁히기
        s += 1
        e -= 1
    else: #넓히기
        s -= 1
        e += 1

print(res)    
'''
