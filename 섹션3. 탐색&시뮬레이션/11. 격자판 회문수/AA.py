#import sys
#sys.stdin=open("input.txt", "r")

number = []
piece = []
cnt = 0

for i in range(7):
    piece = list(map(int, input().split()))

    for j in range(3): #행에서 회문수 카운트
        if piece[j]==piece[j+4] and piece[j+1]==piece[j+3]:
            cnt += 1

    number.append(piece)

number_t = [list(x) for x in zip(*number)]

for i in range(7):
    for j in range(3): #열에서 회문수 카운트
        if number_t[i][j]==number_t[i][j+4] and number_t[i][j+1]==number_t[i][j+3]:
            cnt += 1

print(cnt)

#)
'''
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3): #i열부터
    for j in range(7): #j행까지 5개 회문수 카운트
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]: #회문
            cnt += 1
        
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]: #행/열
                break
            else:
                cnt += 1    

print(cnt)
'''