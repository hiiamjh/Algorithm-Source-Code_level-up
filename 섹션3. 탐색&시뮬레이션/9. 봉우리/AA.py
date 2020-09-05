#import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
bong = [[0]*(n+2)]*(n+2)

for i in range(1,n+1):
    temp = [0]*(n+2)
    temp[1:n+1] = list(map(int, input().split()))
    bong[i] = temp #가장자리 0 초기화

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if (bong[i][j] > bong[i-1][j]) and (bong[i][j] > bong[i+1][j]) and (bong[i][j] > bong[i][j-1]) and (bong[i][j] > bong[i][j+1]):
            cnt += 1

print(cnt)

'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 0초기화
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)
    
# 상하좌우 탐색
cnt = 0

# (i, j) = (-1, 0), (0, 1), (1, 0), (0,-1) => 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1,n+1): #가장자리 제외
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): #4번 반복
            cnt += 1

print(cnt)
'''