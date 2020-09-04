#import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))
val = 0
cnt = 0

for i in range(n):
    for j in range(i, n):
        val += a[j]
        if val >= 3:
            if val == 3:
                cnt += 1
            else:
                pass
            val = 0
            break
print(cnt)

