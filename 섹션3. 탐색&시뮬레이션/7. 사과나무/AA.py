#import sys
#sys.stdin=open("input.txt", "r")

#)틀린 답
n = int(input())
cnt = 0
for i in range(n):
    if i <= n // 2:
        cnt += sum(list(map(int, input().split()))[n//2-i:n//2+i+1])
    else:
        cnt += sum(list(map(int, input().split()))[n//2-(i%2):n//2+(i%2)+1])

print(cnt)

#)포인터 변수 이용
'''
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2 : #구간 넓히기
        s -= 1
        e += 1
    else: #구간 좁히기
        s += 1
        e -= 1

print(res)
'''