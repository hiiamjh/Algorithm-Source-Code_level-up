#import sys
#sys.stdin=open("input.txt", "r")

n = list(range(48,58))
s = input()
answer = ''
cnt = 0

for i in range(len(s)):
    if ord(s[i]) in n:
        answer = answer + s[i]

while True:
    if ord(answer[0])==48:
        answer = answer[1:]
    else:
        print(answer)
        for i in range(1,int(answer)+1):
            if int(answer)%i == 0:
                cnt += 1
        print(cnt)
        break
