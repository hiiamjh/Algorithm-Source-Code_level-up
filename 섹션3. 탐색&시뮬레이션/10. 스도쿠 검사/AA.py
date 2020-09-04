#import sys
#sys.stdin=open("input.txt", "r")

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
