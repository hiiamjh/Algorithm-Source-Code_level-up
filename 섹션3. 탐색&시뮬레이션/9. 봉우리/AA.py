#import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
bong = [[0]*(n+2)]*(n+2)

for i in range(1,n+1):
    temp = [0]*(n+2)
    temp[1:n+1] = list(map(int, input().split()))
    bong[i] = temp

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if (bong[i][j] > bong[i-1][j]) and (bong[i][j] > bong[i+1][j]) and (bong[i][j] > bong[i][j-1]) and (bong[i][j] > bong[i][j+1]):
            cnt += 1

print(cnt)
