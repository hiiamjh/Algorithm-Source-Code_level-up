#import sys
#sys.stdin=open("input.txt", "r")

card = list(range(21))

#) reverse로 역배치
for i in range(10):
    a, b = map(int, input().split())
    temp = card[a:b+1]
    temp.reverse()
    card[a:b+1] = temp

for i in card[1:]:
    print(i, end=' ')


#스와핑
'''
a, b = map(int, input().split())
a, b = b, a
'''

#) 스와핑으로 역배치
'''
for _ in range(10): #시간복잡도 감소
    s, e = map(int, input().split())
    
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)
for x in a:
    print(x, end=' ')
'''