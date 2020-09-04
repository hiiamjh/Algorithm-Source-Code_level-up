#import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
gg = []

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


