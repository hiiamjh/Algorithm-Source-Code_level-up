import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
number = list(map(int, input().split()))

#) 틀린 답
temp = 0
cnt = 0

for i in range(n):
    for j in range(i, n):
        temp += number[j]
        if temp == 3:
            cnt += 1
            temp = 0
            break

    temp = 0

print(cnt)

#) 포인터 변수 이용
'''
lt = 0
rt = 1
tot = number[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += list[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= list[lt] #list[rt] = list[lt]
        lt += 1
    else:
        tot = -list[lt]
        lt += 1
print(cnt)
'''