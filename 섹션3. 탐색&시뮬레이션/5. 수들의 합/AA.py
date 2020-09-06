import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
number = list(map(int, input().split()))

#) 틀린 답
'''
1) temp>3 일 때의 처리
'''
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
    if tot < m: #수들의 합이 m 이하이면
        if rt < n: #리스트가 끝날 때까지
            tot += list[rt] #rt를 이동하며 더하기
            rt += 1
        else:
            break
    elif tot == m: #수들의 합이 m이면
        cnt += 1 #카운트하고
        tot -= list[lt] #list[rt] = list[lt], lt를 이동하기
        lt += 1
    else:
        tot = -list[lt] #수들의 합이 m 이상이면
        lt += 1 #lt를 이동하기
print(cnt)
'''