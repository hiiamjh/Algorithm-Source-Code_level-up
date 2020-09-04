#import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
cnt = 0
for i in range(n):
    if i <= n // 2:
        cnt += sum(list(map(int, input().split()))[n//2-i:n//2+i+1])
    else:
        cnt += sum(list(map(int, input().split()))[n//2-(i%2):n//2+(i%2)+1])

print(cnt)
