#import sys
#sys.stdin=open("input.txt", "r")

n = list(range(48,58))
s = input()
answer = ''
cnt = 0

#ASCII CODE
for i in range(len(s)):
    if ord(s[i]) in n: #숫자
        answer = answer + s[i]

while True:
    if ord(answer[0])==48: #0이면 삭제
        answer = answer[1:]
    else:
        print(answer)
        for i in range(1,int(answer)+1): #약수
            if int(answer)%i == 0:
                cnt += 1
        print(cnt)
        break

#) x.isdigit(): 모든 숫자 / x.isdecimal(): 0~9
'''
s=input()
res=0
for x in s:
    if x.isdecimal():
        res = res*10 + int(x) #숫자화(첫자리의 0 무시)

print(res)
cnt=0
for i in range(1, res+1):
    if res%i == 0:
        cnt += 1
print(cnt)
'''