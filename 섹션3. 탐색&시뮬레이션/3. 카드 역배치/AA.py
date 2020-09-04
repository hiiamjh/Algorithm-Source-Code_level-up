#import sys
#sys.stdin=open("input.txt", "r")

card = list(range(0,21))

for i in range(10):
    a, b = map(int, input().split())
    temp = card[a:b+1]
    temp.reverse()
    card[a:b+1] = temp

for i in card[1:]:
    print(i, end=' ')
