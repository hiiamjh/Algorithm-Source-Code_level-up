#import sys
#sys.stdin=open("input.txt", "r")

number = []
piece = []
cnt = 0

for i in range(7):
    piece = list(map(int, input().split()))

    for j in range(3):
        if piece[j]==piece[j+4] and piece[j+1]==piece[j+3]:
            cnt += 1

    number.append(piece)

number_t = [list(x) for x in zip(*number)]

for i in range(7):
    for j in range(3):
        if number_t[i][j]==number_t[i][j+4] and number_t[i][j+1]==number_t[i][j+3]:
            cnt += 1

print(cnt)
