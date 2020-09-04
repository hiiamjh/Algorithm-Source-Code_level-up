#import sys
#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
number = list(map(int, input().split()))

temp = 0
cnt = 0

for i in range(n):
    for j in range(i, n):
        temp += number[j]
        if temp == 3:
            cnt += 1
            break

    temp = 0

print(cnt)
