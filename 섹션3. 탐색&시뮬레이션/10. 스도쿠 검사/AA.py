#import sys
#sys.stdin=open("input.txt", "r")

#) 틀린 답
sdk = []
piece = []
temp = []

for i in range(9):
    piece = list(map(int, input().split()))
    if len(list(set(piece)))!=9: #행검사
        print("NO")
        break
    sdk.append(piece)

sdk_t = [list(x) for x in zip(*sdk)]

for i in sdk_t:
    if len(list(set(i)))!=9: #열검사
        print("NO")
        break

#) 체크리스트를 이용한 방법
'''
def check(a):
    for i in range(9):
        ch1 = [0]*10 #행검사 => 1~9
        ch2 = [0]*10 #열검사
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
            
    #그룹검사        
    for i in range(3): #전체 행
        for j in range(3): #전체 열
            ch3 = [0]*10
            for k in range(3): #그룹 내 행
                for s in range(3): #그룹 내 열
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True #함수 종료

a = list[map(int, input().split()) for _ in range(9)]
if check(a): #true
    print("YES")
else: #false
    print("NO")
'''