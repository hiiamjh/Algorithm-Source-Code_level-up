#import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())

for i in range(1,n+1):

    s = input()
    s = s.upper()
    cnt = 0

    #)
    for j in range(len(s)//2):
        if s[j]==s[-(j+1)]: cnt += 1

    if cnt == len(s)//2:
        print("#"+str(i)+" YES")

    else:
        print("#"+str(i)+" NO")


    #1): 일치하지 않으면 NO
    '''
    for j in range(len(s)//2):
        if s[j]!=s[-(j+1)]:
            print("#%d NO" %i)
            break
    else: print("#%d YES" %i)
    '''

    #2): 문자열 역순이 같으면 YES
    '''
    if s==s[::-1]: print("#%d YES" %i)
    else: print("#%d NO" %i)
    '''